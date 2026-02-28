// =============================================================================
// Quarto-Typst Bridge (typst-show.typ)
// =============================================================================
// Connects Quarto YAML variables to the engineering report template.
// Uses Pandoc template syntax ($variable$) for Quarto integration.
//
// Theme colors and branding are passed via params.theme-* YAML keys.
// Any param not provided falls back to the template's built-in defaults.
// =============================================================================

// Import path is relative to the generated .typ output file
#import "_extensions/engineering-report/typst-template.typ": engineering-report

#show: doc => engineering-report(
  // --- Content (from standard Quarto front matter) ---
  title: [$title$],
$if(subtitle)$
  subtitle: [$subtitle$],
$endif$
$if(author)$
  author: [$author$],
$endif$
$if(company)$
  company: [$company$],
$endif$
$if(date)$
  date: [$date$],
$endif$
$if(params.report-logo)$
  logo: "$params.report-logo$",
$endif$
$if(params.document_version)$
  doc-version: [$params.document_version$],
$else$
  doc-version: [1.0],
$endif$
$if(params.confidentiality)$
  classification: "$params.confidentiality$",
$else$
  classification: "CONFIDENTIAL",
$endif$
$if(params.analysis_id)$
  analysis-id: [$params.analysis_id$],
$endif$
$if(params.software_version)$
  software-version: [$params.software_version$],
$endif$

  // --- Theme Colors (from params.theme-*) ---
  // Colors are passed without # prefix to avoid Pandoc escaping
$if(params.theme-primary)$
  primary-color: rgb("#$params.theme-primary$"),
$endif$
$if(params.theme-accent)$
  accent-color: rgb("#$params.theme-accent$"),
$endif$
$if(params.theme-secondary)$
  secondary-color: rgb("#$params.theme-secondary$"),
$endif$
$if(params.theme-gray)$
  gray-color: rgb("#$params.theme-gray$"),
$endif$
$if(params.theme-light-gray)$
  light-gray-color: rgb("#$params.theme-light-gray$"),
$endif$
$if(params.theme-dark)$
  dark-color: rgb("#$params.theme-dark$"),
$endif$

  // --- Typography (from params) ---
$if(params.body-font)$
  body-font: ("$params.body-font$",),
$endif$
$if(params.heading-font)$
  heading-font: ("$params.heading-font$",),
$endif$

  // --- Branding (from params) ---
$if(params.report-label)$
  report-label: "$params.report-label$",
$endif$
$if(params.copyright-text)$
  copyright-text: "$params.copyright-text$",
$endif$
$if(params.software-name)$
  software-name: "$params.software-name$",
$endif$

$if(toc)$
  toc: true,
$else$
  toc: false,
$endif$
$if(toc-depth)$
  toc-depth: $toc-depth$,
$endif$
  doc,
)
