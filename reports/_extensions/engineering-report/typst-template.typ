// =============================================================================
// Engineering Report Template (Reusable)
// =============================================================================
// Professional engineering report template with parameterized theming.
// Structural layout is fixed; colors, fonts, and branding are configurable
// through Quarto YAML parameters via the typst-show.typ bridge.
//
// Based on VAG RIKO Control Valve Report Template.
// Inspired by basic-report template (https://typst.app/universe/package/basic-report)
// =============================================================================

// Import Hydra for running headers
#import "@preview/hydra:0.6.1": hydra

// Classification badge colors (fixed — these are universal semantic colors)
#let classification-colors = (
  "CONFIDENTIAL": rgb("#b91c1c"),
  "INTERNAL": rgb("#d97706"),
  "PUBLIC": rgb("#059669"),
)

// =============================================================================
// Main Template Function
// =============================================================================
#let engineering-report(
  // --- Content Parameters (from document front matter) ---
  title: none,
  subtitle: none,
  author: none,
  company: none,
  date: none,
  logo: none,
  doc-version: "1.0",
  classification: "CONFIDENTIAL",
  analysis-id: none,
  software-version: none,
  toc: true,
  toc-depth: 2,

  // --- Theme Parameters (override per project) ---
  // Colors
  primary-color: rgb("#00a651"),       // Headings H2, accents, decorative lines
  accent-color: rgb("#006837"),        // H1, title page, table headers, title bar
  secondary-color: rgb("#007dc5"),     // Reserved for future use (links, callouts). Not yet wired to any element.
  gray-color: rgb("#58595b"),          // Body secondary text, captions, footer
  light-gray-color: rgb("#e8e8e8"),    // Table header fill, borders
  dark-color: rgb("#2c2c2c"),          // Body text, H3

  // Typography
  body-font: ("Vollkorn", "Georgia", "Times New Roman", "serif"),
  heading-font: ("Ubuntu", "Lato", "Arial", "sans-serif"),

  // Branding
  report-label: "ENGINEERING REPORT",  // Title page label (e.g. "SIZING REPORT")
  copyright-text: "All rights reserved. Unauthorized distribution prohibited.",
  software-name: "Engineering Analysis System",

  // --- Document Body ---
  doc,
) = {
  // Derived theme colors
  let alt-row-color = light-gray-color.lighten(60%)
  let label-fill-color = light-gray-color.lighten(40%)

  // Reusable copyright notice
  let copyright-notice = if company != none {
    [© #company. #copyright-text]
  } else {
    [#copyright-text]
  }

  // ---------------------------------------------------------------------------
  // Page Setup
  // ---------------------------------------------------------------------------
  set page(
    paper: "a4",
    margin: (
      top: 28mm,
      bottom: 22mm,
      left: 22mm,
      right: 22mm,
    ),
    header: context {
      // No header on first page (title page)
      if counter(page).get().first() > 1 {
        set text(size: 8pt, fill: gray-color)
        grid(
          columns: (1fr, auto, 1fr),
          align: (left, center, right),
          [#if analysis-id != none { text(weight: "medium")[#analysis-id] }],
          [#box(
            fill: classification-colors.at(classification, default: rgb("#666")),
            inset: (x: 6pt, y: 2pt),
            radius: 2pt,
          )[#text(fill: white, size: 7pt, weight: "bold")[#classification]]],
          [],
        )
        v(-2pt)
        line(length: 100%, stroke: 0.75pt + primary-color)
      }
    },
    footer: context {
      line(length: 100%, stroke: 0.5pt + light-gray-color)
      v(3pt)
      set text(size: 7pt, fill: gray-color)
      grid(
        columns: (1fr, auto, 1fr),
        align: (left, center, right),
        [],
        [#copyright-notice],
        [Page #counter(page).display() of #counter(page).final().first()],
      )
    },
  )

  // ---------------------------------------------------------------------------
  // Typography
  // ---------------------------------------------------------------------------
  set text(
    font: body-font,
    size: 10pt,
    fill: dark-color,
  )

  set par(
    justify: true,
    leading: 0.65em,
    first-line-indent: 0pt,
  )

  // Heading Styles
  set heading(numbering: "1.1.1")

  show heading.where(level: 1): it => {
    v(1.2em)
    block(below: 0.8em)[
      #text(font: heading-font, size: 16pt, weight: "bold", fill: accent-color)[#it]
    ]
  }

  show heading.where(level: 2): it => {
    v(0.8em)
    block(below: 0.5em)[
      #text(font: heading-font, size: 12pt, weight: "bold", fill: primary-color)[#it]
    ]
  }

  show heading.where(level: 3): it => {
    v(0.5em)
    block(below: 0.3em)[
      #text(font: heading-font, size: 10.5pt, weight: "bold", fill: dark-color)[#it]
    ]
  }

  // ---------------------------------------------------------------------------
  // Professional Table Styling
  // ---------------------------------------------------------------------------
  // Table defaults (inner) — sets cell-level properties
  show table: set table(
    stroke: (x, y) => (
      top: if y == 0 { none } else if y == 1 { 0.75pt + gray-color } else { 0.5pt + light-gray-color },
      bottom: 0.5pt + light-gray-color,
      left: none,
      right: none,
    ),
    inset: (x: 8pt, y: 6pt),
    fill: (x, y) => if y == 0 { light-gray-color } else if calc.odd(y) { white } else { alt-row-color },
  )

  // Table wrapper (outer) — adds top/bottom accent border
  show table: it => {
    set text(size: 9pt)
    block(
      stroke: (
        top: 2pt + accent-color,
        bottom: 1pt + gray-color,
        left: none,
        right: none,
      ),
      inset: 0pt,
      it,
    )
  }

  // Table header row styling
  show table.cell.where(y: 0): it => {
    text(weight: "bold", fill: accent-color, size: 9pt)[#it]
  }

  // Code Block Styling
  show raw.where(block: true): it => {
    set text(size: 8.5pt)
    block(
      fill: alt-row-color,
      stroke: 0.5pt + light-gray-color,
      inset: 10pt,
      radius: 3pt,
      width: 100%,
      it,
    )
  }

  // ---------------------------------------------------------------------------
  // Figure Styling
  // ---------------------------------------------------------------------------
  show figure: it => {
    set align(center)
    block(
      width: 100%,
      breakable: false,
    )[
      #it.body
      #v(0.5em)
      #if it.caption != none {
        block(
          width: 90%,
          inset: (x: 10pt, y: 6pt),
        )[
          #text(size: 9pt, fill: gray-color)[
            #text(weight: "bold", fill: accent-color)[#it.supplement #it.counter.display():]
            #it.caption.body
          ]
        ]
      }
    ]
    v(1em)
  }

  // ---------------------------------------------------------------------------
  // TITLE PAGE
  // ---------------------------------------------------------------------------
  page(header: none, footer: none)[
    // Header bar with logo
    #block(width: 100%)[
      #grid(
        columns: (1fr, auto),
        align: (left + horizon, right),
        [
          #box(
            fill: accent-color,
            inset: (x: 12pt, y: 8pt),
            radius: (top-right: 4pt, bottom-right: 4pt),
          )[
            #text(fill: white, weight: "bold", size: 11pt, tracking: 0.5pt)[#report-label]
          ]
        ],
        [
          #if logo != none {
            image(logo, width: 50mm)
          }
        ],
      )
    ]

    #v(20mm)

    // Main Title
    #align(center)[
      #block(width: 100%)[
        #text(size: 28pt, weight: "bold", fill: accent-color, tracking: -0.5pt)[#title]
        #v(6mm)
        #if subtitle != none {
          text(size: 14pt, fill: gray-color, style: "italic")[#subtitle]
        }
      ]
    ]

    #v(15mm)

    // Classification Badge
    #align(center)[
      #box(
        fill: classification-colors.at(classification, default: rgb("#666")),
        inset: (x: 20pt, y: 10pt),
        radius: 4pt,
        stroke: 1pt + classification-colors.at(classification, default: rgb("#666")).darken(20%),
      )[
        #text(fill: white, weight: "bold", size: 12pt, tracking: 1pt)[#upper(classification)]
      ]
    ]

    #v(20mm)

    // Document Control Table
    #align(center)[
      #block(width: 85%)[
        #table(
          columns: (140pt, 1fr),
          align: (left, left),
          stroke: none,
          inset: (x: 12pt, y: 10pt),
          fill: (x, y) => if x == 0 { label-fill-color } else { white },

          // Header
          table.cell(colspan: 2, fill: accent-color)[
            #text(fill: white, weight: "bold", size: 10pt)[DOCUMENT CONTROL]
          ],

          // Data rows
          [#text(weight: "bold", fill: dark-color)[Document No.]],
          [#text(weight: "medium")[#if analysis-id != none { analysis-id } else { "---" }]],
          [#text(weight: "bold", fill: dark-color)[Version]], [#doc-version],
          [#text(weight: "bold", fill: dark-color)[Classification]],
          [#text(fill: classification-colors.at(classification, default: rgb("#666")), weight: "bold")[#classification]],
          [#text(weight: "bold", fill: dark-color)[Prepared by]], [#author #h(1em) #text(fill: gray-color)[--- #company]],
          [#text(weight: "bold", fill: dark-color)[Report Generated]], [#date],
          [#text(weight: "bold", fill: dark-color)[Software Version]],
          [#if software-version != none { software-version } else { "---" }],
        )
      ]
    ]

    #v(1fr)

    // Footer
    #block(width: 100%)[
      #line(length: 100%, stroke: 1pt + primary-color)
      #v(4mm)
      #align(center)[
        #text(size: 8pt, fill: gray-color)[
          This document was generated by #text(weight: "bold")[#software-name]
        ]
        #v(2mm)
        #text(size: 7pt, fill: gray-color.lighten(20%))[
          #copyright-notice
        ]
      ]
    ]
  ]

  // ---------------------------------------------------------------------------
  // Table of Contents
  // ---------------------------------------------------------------------------
  if toc {
    block(inset: (left: 0pt, right: 0pt))[
      #text(size: 16pt, weight: "bold", fill: accent-color)[Table of Contents]
      #v(0.8em)
      #line(length: 40%, stroke: 2pt + primary-color)
    ]
    v(1em)
    outline(
      title: none,
      indent: 1.5em,
      depth: toc-depth,
    )
    pagebreak()
  }

  // ---------------------------------------------------------------------------
  // Document Body
  // ---------------------------------------------------------------------------
  doc
}
