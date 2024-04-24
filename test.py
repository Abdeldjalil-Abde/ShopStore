# import re


# def extract_classes_with_code(css_code):
#     # Regular expression pattern to match CSS class names and their code
#     pattern = r'\.([a-zA-Z0-9_-]+)\s*{([^}]*)}'
#     # Find all matches of the pattern in the CSS code
#     matches = re.findall(pattern, css_code, re.DOTALL)
#     # Construct a dictionary of class names and their corresponding CSS code
#     class_dict = {class_name: class_code.strip()
#                   for class_name, class_code in matches}
#     return class_dict


# def extract_classes(css_code):
#     # Regular expression pattern to match CSS class names
#     pattern = r'class="([^"]+)"'
#     # Find all matches of the pattern in the CSS code
#     matches = re.findall(pattern, css_code)
#     # Remove duplicates and return the list of class names
#     return list(set(matches))


# # Example CSS code
# css_code = """
# ['btn btn-info btn-block btn-lg', ' fa-long-arrow-alt-right ms-2', 'fw-normal ', 'card bg-primary text-white rounded-3', 
# 'card  mb-lg-0', ' fa-angle-down mt-1', ' p-4', '', ' ', 'row', ' ', 
# ' flex-row ', 'col-lg-7', 'text-body', 'ms-3', 'col-lg-5', 'txt', 'text-muted', 
# ' fa-long-arrow-alt-left ', 'my-4', ' ', '', 
# '   ', ' fa-cc-paypal fa-2x', '  ',
#  'mb-1', '', ' fa-cc-amex fa-2x ', 'img-fluid rounded-3', ' fa-cc-mastercard fa-2x ', 
#  ' fa-trash-alt', ' fa-cc-visa fa-2x ', 'card ', 'text-white', '', ' h-custom', 
#  'container py-5 ', 'center']
# """

# # Extract classes with their code from the CSS code
# # class_dict = extract_classes_with_code(css_code)
# # # Print the extracted classes with their code
# # print("Classes present in the CSS code with their code:")
# # for class_name, class_code in class_dict.items():
# #     print(f"Class: {class_name}")
# #     print(f"Code: {class_code}\n")
# # Extract classes from the CSS code
# classes = extract_classes(css_code)
# # Print the extracted classes
# print("Classes present in the CSS code:")
# print(classes)
# words = ['col-lg-7', 'col-lg-5', 'd-flex', 'justify-content-between', 'small', 'mb-0', 
#          'text-muted', 'h-100', 'h-custom', 'fas', 'fa-trash-alt', 'container', 'py-5', 'text-body', 
#          'fab fa-cc-amex',  'me-2', 'mb-1', 'align-items-center', 'mb-4', 'fa-cc-mastercard ','fa-2x', 
#          'mb-2', 'mb-3', 'card-body', ' fa-cc-paypal','flex-row ', 'card',  'mb-lg-0',  
#          'fa-long-arrow-alt-left', ' bg-primary', 'text-white', ' fa-angle-down', 'mt-1', 
#          'txt', 'fw-normal', 'p-4', 'my-4', 'center', 'fa-cc-visa ', 'fa-long-arrow-alt-right',
#          'ms-2', 'btn', 'btn-info', 'btn-block', 'btn-lg', 'row', 'img-fluid', 'rounded-3', 'ms-3']

# unique_words = list(set(words))

# print("List with duplicate words removed:")
# print(unique_words)

import re

def extract_css_for_classes(css_code, classes):
    class_patterns = '|'.join(classes)
    pattern = rf'(\.{class_patterns})\s*{{([^}}]*)}}'
    matches = re.findall(pattern, css_code, re.MULTILINE)
    class_dict = {class_name.strip(): class_code.strip() for class_name, class_code in matches}
    return class_dict

# Example CSS code
css_code = """
:root,
[data-mdb-theme=light] {
    --mdb-red: #f44336;
    --mdb-pink: #e91e63;
    --mdb-purple: #9c27b0;
    --mdb-indigo: #3f51b5;
    --mdb-blue: #2196f3;
    --mdb-cyan: #00bcd4;
    --mdb-teal: #009688;
    --mdb-green: #4caf50;
    --mdb-yellow: #ffeb3b;
    --mdb-orange: #ff9800;
    --mdb-white: #fff;
    --mdb-black: #000;
    --mdb-gray: #757575;
    --mdb-gray-dark: #4f4f4f;
    --mdb-gray-50: #fbfbfb;
    --mdb-gray-100: #f5f5f5;
    --mdb-gray-200: #eeeeee;
    --mdb-gray-300: #e0e0e0;
    --mdb-gray-400: #bdbdbd;
    --mdb-gray-500: #9e9e9e;
    --mdb-gray-600: #757575;
    --mdb-gray-700: #616161;
    --mdb-gray-800: #4f4f4f;
    --mdb-gray-900: #262626;
    --mdb-primary: #3b71ca;
    --mdb-secondary: #9fa6b2;
    --mdb-success: #14a44d;
    --mdb-danger: #dc4c64;
    --mdb-warning: #e4a11b;
    --mdb-info: #54b4d3;
    --mdb-light: #fbfbfb;
    --mdb-dark: #332d2d;
    --mdb-primary-rgb: 59, 113, 202;
    --mdb-secondary-rgb: 159, 166, 178;
    --mdb-success-rgb: 20, 164, 77;
    --mdb-danger-rgb: 220, 76, 100;
    --mdb-warning-rgb: 228, 161, 27;
    --mdb-info-rgb: 84, 180, 211;
    --mdb-light-rgb: 251, 251, 251;
    --mdb-dark-rgb: 51, 45, 45;
    --mdb-primary-text-emphasis: #2f5aa2;
    --mdb-secondary-text-emphasis: #404247;
    --mdb-success-text-emphasis: #0c622e;
    --mdb-info-text-emphasis: #3b7e94;
    --mdb-warning-text-emphasis: #896110;
    --mdb-danger-text-emphasis: #b03d50;
    --mdb-light-text-emphasis: #616161;
    --mdb-dark-text-emphasis: #eeeeee;
    --mdb-primary-bg-subtle: #e2eaf7;
    --mdb-secondary-bg-subtle: #f1f2f3;
    --mdb-success-bg-subtle: #dcf1e4;
    --mdb-info-bg-subtle: #e5f4f8;
    --mdb-warning-bg-subtle: #fbf1dd;
    --mdb-danger-bg-subtle: #fae4e8;
    --mdb-light-bg-subtle: #f5f5f5;
    --mdb-dark-bg-subtle: #262626;
    --mdb-primary-border-subtle: #b1c6ea;
    --mdb-secondary-border-subtle: #d9dbe0;
    --mdb-success-border-subtle: #a1dbb8;
    --mdb-info-border-subtle: #bbe1ed;
    --mdb-warning-border-subtle: #f4d9a4;
    --mdb-danger-border-subtle: #f1b7c1;
    --mdb-light-border-subtle: #eeeeee;
    --mdb-dark-border-subtle: #9e9e9e;
    --mdb-white-rgb: 255, 255, 255;
    --mdb-black-rgb: 0, 0, 0;
    --mdb-font-sans-serif: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", "Noto Sans", "Liberation Sans", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
    --mdb-font-monospace: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
    --mdb-gradient: linear-gradient(180deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0));
    --mdb-body-font-family: var(--mdb-font-roboto);
    --mdb-body-font-size: 1rem;
    --mdb-body-font-weight: 400;
    --mdb-body-line-height: 1.6;
    --mdb-body-color: #4f4f4f;
    --mdb-body-color-rgb: 79, 79, 79;
    --mdb-body-bg: #fff;
    --mdb-body-bg-rgb: 255, 255, 255;
    --mdb-emphasis-color: #000;
    --mdb-emphasis-color-rgb: 0, 0, 0;
    --mdb-secondary-color: rgba(79, 79, 79, 0.75);
    --mdb-secondary-color-rgb: 79, 79, 79;
    --mdb-secondary-bg: #eeeeee;
    --mdb-secondary-bg-rgb: 238, 238, 238;
    --mdb-tertiary-color: rgba(79, 79, 79, 0.5);
    --mdb-tertiary-color-rgb: 79, 79, 79;
    --mdb-tertiary-bg: #fbfbfb;
    --mdb-tertiary-bg-rgb: 251, 251, 251;
    --mdb-heading-color: inherit;
    --mdb-link-color: #3b71ca;
    --mdb-link-color-rgb: 59, 113, 202;
    --mdb-link-decoration: none;
    --mdb-link-hover-color: #386bc0;
    --mdb-link-hover-color-rgb: 56, 107, 192;
    --mdb-link-hover-decoration: none;
    --mdb-code-color: #e91e63;
    --mdb-highlight-color: #4f4f4f;
    --mdb-highlight-bg: #fff9c4;
    --mdb-border-width: 1px;
    --mdb-border-style: solid;
    --mdb-border-color: #e0e0e0;
    --mdb-border-color-translucent: rgba(0, 0, 0, 0.175);
    --mdb-border-radius: 0.25rem;
    --mdb-border-radius-sm: 0.25rem;
    --mdb-border-radius-lg: 0.5rem;
    --mdb-border-radius-xl: 1rem;
    --mdb-border-radius-xxl: 2rem;
    --mdb-border-radius-2xl: var(--mdb-border-radius-xxl);
    --mdb-border-radius-pill: 50rem;
    --mdb-box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
    --mdb-box-shadow-sm: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
    --mdb-box-shadow-lg: 0 1rem 3rem rgba(0, 0, 0, 0.175);
    --mdb-box-shadow-inset: inset 0 1px 2px rgba(0, 0, 0, 0.075);
    --mdb-focus-ring-width: 0.25rem;
    --mdb-focus-ring-opacity: 0.25;
    --mdb-focus-ring-color: rgba(59, 113, 202, 0.25);
    --mdb-form-valid-color: #14a44d;
    --mdb-form-valid-border-color: #14a44d;
    --mdb-form-invalid-color: #dc4c64;
    --mdb-form-invalid-border-color: #dc4c64
}

[data-mdb-theme=dark] {
    color-scheme: dark;
    --mdb-body-color: #fff;
    --mdb-body-color-rgb: 255, 255, 255;
    --mdb-body-bg: #303030;
    --mdb-body-bg-rgb: 48, 48, 48;
    --mdb-emphasis-color: #fff;
    --mdb-emphasis-color-rgb: 255, 255, 255;
    --mdb-secondary-color: rgba(255, 255, 255, 0.75);
    --mdb-secondary-color-rgb: 255, 255, 255;
    --mdb-secondary-bg: #4f4f4f;
    --mdb-secondary-bg-rgb: 79, 79, 79;
    --mdb-tertiary-color: rgba(255, 255, 255, 0.5);
    --mdb-tertiary-color-rgb: 255, 255, 255;
    --mdb-tertiary-bg: #3b3b3b;
    --mdb-tertiary-bg-rgb: 59, 59, 59;
    --mdb-primary-text-emphasis: #628dd5;
    --mdb-secondary-text-emphasis: #d9dbe0;
    --mdb-success-text-emphasis: #72c894;
    --mdb-info-text-emphasis: #87cbe0;
    --mdb-warning-text-emphasis: #efc776;
    --mdb-danger-text-emphasis: #e37083;
    --mdb-light-text-emphasis: #f5f5f5;
    --mdb-dark-text-emphasis: #eeeeee;
    --mdb-primary-bg-subtle: #0c1728;
    --mdb-secondary-bg-subtle: #202124;
    --mdb-success-bg-subtle: #04210f;
    --mdb-info-bg-subtle: #11242a;
    --mdb-warning-bg-subtle: #2e2005;
    --mdb-danger-bg-subtle: #2c0f14;
    --mdb-light-bg-subtle: #4f4f4f;
    --mdb-dark-bg-subtle: #262626;
    --mdb-primary-border-subtle: #234479;
    --mdb-secondary-border-subtle: #5f646b;
    --mdb-success-border-subtle: #0c622e;
    --mdb-info-border-subtle: #326c7f;
    --mdb-warning-border-subtle: #896110;
    --mdb-danger-border-subtle: #842e3c;
    --mdb-light-border-subtle: #616161;
    --mdb-dark-border-subtle: #4f4f4f;
    --mdb-heading-color: inherit;
    --mdb-link-color: #89aadf;
    --mdb-link-hover-color: #8faee1;
    --mdb-link-color-rgb: 137, 170, 223;
    --mdb-link-hover-color-rgb: 143, 174, 225;
    --mdb-code-color: #f278a1;
    --mdb-highlight-color: #fff;
    --mdb-highlight-bg: #f9a825;
    --mdb-border-color: rgba(255, 255, 255, 0.12);
    --mdb-border-color-translucent: rgba(255, 255, 255, 0.15);
    --mdb-form-valid-color: #81c784;
    --mdb-form-valid-border-color: #81c784;
    --mdb-form-invalid-color: #e57373;
    --mdb-form-invalid-border-color: #e57373
}

*,
*::before,
*::after {
    box-sizing: border-box
}

@media(prefers-reduced-motion: no-preference) {
    :root {
        scroll-behavior: smooth
    }
}

hr {
    margin: 1rem 0;
    color: inherit;
    border: 0;
    border-top: var(--mdb-border-width) solid;
    opacity: .25
}

h6,
.h6,
h5,
.h5,
h4,
.h4,
h3,
.h3,
h2,
.h2,
h1,
.h1 {
    margin-top: 0;
    margin-bottom: .5rem;
    font-weight: 500;
    line-height: 1.2;
    color: var(--mdb-heading-color)
}

h1,
.h1 {
    font-size: calc(1.375rem + 1.5vw)
}


h2,
.h2 {
    font-size: calc(1.325rem + 0.9vw)
}


h3,
.h3 {
    font-size: calc(1.3rem + 0.6vw)
}

@media(min-width: 1200px) {

    h3,
    .h3 {
        font-size: 1.75rem
    }
}

h4,
.h4 {
    font-size: calc(1.275rem + 0.3vw)
}


h5,
.h5 {
    font-size: 1.25rem
}

h6,
.h6 {
    font-size: 1rem
}

p {
    margin-top: 0;
    margin-bottom: 1rem
}

a:hover {
    --mdb-link-color-rgb: var(--mdb-link-hover-color-rgb);
    text-decoration: none
}

a:not([href]):not([class]),
a:not([href]):not([class]):hover {
    color: inherit;
    text-decoration: none
}

pre,
code,
kbd,
samp {
    font-family: var(--mdb-font-monospace);
    font-size: 1em
}

pre {
    display: block;
    margin-top: 0;
    margin-bottom: 1rem;
    overflow: auto;
    font-size: 0.875em
}

pre code {
    font-size: inherit;
    color: inherit;
    word-break: normal
}

code {
    font-size: 0.875em;
    color: var(--mdb-code-color);
    word-wrap: break-word
}

a>code {
    color: inherit
}

kbd {
    padding: .1875rem .375rem;
    font-size: 0.875em;
    color: var(--mdb-body-bg);
    background-color: var(--mdb-body-color);
    border-radius: .25rem
}

kbd kbd {
    padding: 0;
    font-size: 1em
}

figure {
    margin: 0 0 1rem
}

img,
svg {
    vertical-align: middle
}

table {
    caption-side: bottom;
    border-collapse: collapse
}

caption {
    padding-top: 1rem;
    padding-bottom: 1rem;
    color: var(--mdb-secondary-color);
    text-align: left
}

th {
    text-align: inherit;
    text-align: -webkit-match-parent
}

thead,
tbody,
tfoot,
tr,
td,
th {
    border-color: inherit;
    border-style: solid;
    border-width: 0
}

label {
    display: inline-block
}

button {
    border-radius: 0
}

button:focus:not(:focus-visible) {
    outline: 0
}

input,
button,
select,
optgroup,
textarea {
    margin: 0;
    font-family: inherit;
    font-size: inherit;
    line-height: inherit
}

button,
select {
    text-transform: none
}

[role=button] {
    cursor: pointer
}

select {
    word-wrap: normal
}

select:disabled {
    opacity: 1
}

[list]:not([type=date]):not([type=datetime-local]):not([type=month]):not([type=week]):not([type=time])::-webkit-calendar-picker-indicator {
    display: none !important
}

button,
[type=button],
[type=reset],
[type=submit] {
    -webkit-appearance: button
}

button:not(:disabled),
[type=button]:not(:disabled),
[type=reset]:not(:disabled),
[type=submit]:not(:disabled) {
    cursor: pointer
}

::-moz-focus-inner {
    padding: 0;
    border-style: none
}

textarea {
    resize: vertical
}

fieldset {
    min-width: 0;
    padding: 0;
    margin: 0;
    border: 0
}

legend {
    float: left;
    width: 100%;
    padding: 0;
    margin-bottom: .5rem;
    font-size: calc(1.275rem + 0.3vw);
    line-height: inherit
}

@media(min-width: 1200px) {
    legend {
        font-size: 1.5rem
    }
}

legend+* {
    clear: left
}

::-webkit-datetime-edit-fields-wrapper,
::-webkit-datetime-edit-text,
::-webkit-datetime-edit-minute,
::-webkit-datetime-edit-hour-field,
::-webkit-datetime-edit-day-field,
::-webkit-datetime-edit-month-field,
::-webkit-datetime-edit-year-field {
    padding: 0
}

::-webkit-inner-spin-button {
    height: auto
}

[type=search] {
    -webkit-appearance: textfield;
    outline-offset: -2px
}

::-webkit-search-decoration {
    -webkit-appearance: none
}

::-webkit-color-swatch-wrapper {
    padding: 0
}

::file-selector-button {
    font: inherit;
    -webkit-appearance: button
}

output {
    display: inline-block
}

iframe {
    border: 0
}

summary {
    display: list-item;
    cursor: pointer
}

progress {
    vertical-align: baseline
}

[hidden] {
    display: none !important
}

.lead {
    font-size: 1.25rem;
    font-weight: 300
}

.display-1 {
    font-size: calc(1.625rem + 4.5vw);
    font-weight: 300;
    line-height: 1.2
}

@media(min-width: 1200px) {
    .display-1 {
        font-size: 5rem
    }
}

.display-2 {
    font-size: calc(1.575rem + 3.9vw);
    font-weight: 300;
    line-height: 1.2
}

@media(min-width: 1200px) {
    .display-2 {
        font-size: 4.5rem
    }
}

.display-3 {
    font-size: calc(1.525rem + 3.3vw);
    font-weight: 300;
    line-height: 1.2
}

@media(min-width: 1200px) {
    .display-3 {
        font-size: 4rem
    }
}

.display-4 {
    font-size: calc(1.475rem + 2.7vw);
    font-weight: 300;
    line-height: 1.2
}

@media(min-width: 1200px) {
    .display-4 {
        font-size: 3.5rem
    }
}

.display-5 {
    font-size: calc(1.425rem + 2.1vw);
    font-weight: 300;
    line-height: 1.2
}

@media(min-width: 1200px) {
    .display-5 {
        font-size: 3rem
    }
}

.display-6 {
    font-size: calc(1.375rem + 1.5vw);
    font-weight: 300;
    line-height: 1.2
}

@media(min-width: 1200px) {
    .display-6 {
        font-size: 2.5rem
    }
}

.list-unstyled {
    padding-left: 0;
    list-style: none
}

.list-inline {
    padding-left: 0;
    list-style: none
}

.list-inline-item {
    display: inline-block
}

.list-inline-item:not(:last-child) {
    margin-right: .5rem
}

.initialism {
    font-size: 0.875em;
    text-transform: uppercase
}

.blockquote {
    margin-bottom: 1rem;
    font-size: 1.25rem
}

.blockquote>:last-child {
    margin-bottom: 0
}

.blockquote-footer {
    margin-top: -1rem;
    margin-bottom: 1rem;
    font-size: 0.875em;
    color: #757575
}

.blockquote-footer::before {
    content: "â€”آ "
}

.img-fluid {
    max-width: 100%;
    height: auto
}

.img-thumbnail {
    padding: .25rem;
    background-color: var(--mdb-body-bg);
    border: var(--mdb-border-width) solid var(--mdb-border-color);
    border-radius: var(--mdb-border-radius);
    box-shadow: var(--mdb-box-shadow-sm);
    max-width: 100%;
    height: auto
}

.figure {
    display: inline-block
}

.figure-img {
    margin-bottom: .5rem;
    line-height: 1
}

.figure-caption {
    font-size: 0.875em;
    color: var(--mdb-secondary-color)
}

.container,
.container-fluid,
.container-xxl,
.container-xl,
.container-lg,
.container-md,
.container-sm {
    --mdb-gutter-x: 1.5rem;
    --mdb-gutter-y: 0;
    width: 100%;
    padding-right: calc(var(--mdb-gutter-x)*.5);
    padding-left: calc(var(--mdb-gutter-x)*.5);
    margin-right: auto;
    margin-left: auto
}

@media(min-width: 576px) {

    .container-sm,
    .container {
        max-width: 540px
    }
}

@media(min-width: 768px) {

    .container-md,
    .container-sm,
    .container {
        max-width: 720px
    }
}

@media(min-width: 992px) {

    .container-lg,
    .container-md,
    .container-sm,
    .container {
        max-width: 960px
    }
}

@media(min-width: 1200px) {

    .container-xl,
    .container-lg,
    .container-md,
    .container-sm,
    .container {
        max-width: 1140px
    }
}

@media(min-width: 1400px) {

    .container-xxl,
    .container-xl,
    .container-lg,
    .container-md,
    .container-sm,
    .container {
        max-width: 1320px
    }
}

:root {
    --mdb-breakpoint-xs: 0;
    --mdb-breakpoint-sm: 576px;
    --mdb-breakpoint-md: 768px;
    --mdb-breakpoint-lg: 992px;
    --mdb-breakpoint-xl: 1200px;
    --mdb-breakpoint-xxl: 1400px
}

.row {
    --mdb-gutter-x: 1.5rem;
    --mdb-gutter-y: 0;
    display: flex;
    flex-wrap: wrap;
    margin-top: calc(-1*var(--mdb-gutter-y));
    margin-right: calc(-0.5*var(--mdb-gutter-x));
    margin-left: calc(-0.5*var(--mdb-gutter-x))
}

.row>* {
    flex-shrink: 0;
    width: 100%;
    max-width: 100%;
    padding-right: calc(var(--mdb-gutter-x)*.5);
    padding-left: calc(var(--mdb-gutter-x)*.5);
    margin-top: var(--mdb-gutter-y)
}

.col {
    flex: 1 0 0%
}



@media(min-width: 992px) {
    .col-lg {
        flex: 1 0 0%
    }

    .row-cols-lg-auto>* {
        flex: 0 0 auto;
        width: auto
    }

    .row-cols-lg-1>* {
        flex: 0 0 auto;
        width: 100%
    }

    .row-cols-lg-2>* {
        flex: 0 0 auto;
        width: 50%
    }

    .row-cols-lg-3>* {
        flex: 0 0 auto;
        width: 33.33333333%
    }

    .row-cols-lg-4>* {
        flex: 0 0 auto;
        width: 25%
    }

    .row-cols-lg-5>* {
        flex: 0 0 auto;
        width: 20%
    }

    .row-cols-lg-6>* {
        flex: 0 0 auto;
        width: 16.66666667%
    }

    .col-lg-auto {
        flex: 0 0 auto;
        width: auto
    }

    .col-lg-1 {
        flex: 0 0 auto;
        width: 8.33333333%
    }

    .col-lg-2 {
        flex: 0 0 auto;
        width: 16.66666667%
    }

    .col-lg-3 {
        flex: 0 0 auto;
        width: 25%
    }

    .col-lg-4 {
        flex: 0 0 auto;
        width: 33.33333333%
    }

    .col-lg-5 {
        flex: 0 0 auto;
        width: 41.66666667%
    }

    .col-lg-6 {
        flex: 0 0 auto;
        width: 50%
    }

    .col-lg-7 {
        flex: 0 0 auto;
        width: 58.33333333%
    }

    .col-lg-8 {
        flex: 0 0 auto;
        width: 66.66666667%
    }

    .col-lg-9 {
        flex: 0 0 auto;
        width: 75%
    }

    .col-lg-10 {
        flex: 0 0 auto;
        width: 83.33333333%
    }

    .col-lg-11 {
        flex: 0 0 auto;
        width: 91.66666667%
    }

    .col-lg-12 {
        flex: 0 0 auto;
        width: 100%
    }

    .offset-lg-0 {
        margin-left: 0
    }

    .offset-lg-1 {
        margin-left: 8.33333333%
    }

    .offset-lg-2 {
        margin-left: 16.66666667%
    }

    .offset-lg-3 {
        margin-left: 25%
    }

    .offset-lg-4 {
        margin-left: 33.33333333%
    }

    .offset-lg-5 {
        margin-left: 41.66666667%
    }

    .offset-lg-6 {
        margin-left: 50%
    }

    .offset-lg-7 {
        margin-left: 58.33333333%
    }

    .offset-lg-8 {
        margin-left: 66.66666667%
    }

    .offset-lg-9 {
        margin-left: 75%
    }

    .offset-lg-10 {
        margin-left: 83.33333333%
    }

    .offset-lg-11 {
        margin-left: 91.66666667%
    }

    .g-lg-0,
    .gx-lg-0 {
        --mdb-gutter-x: 0
    }

    .g-lg-0,
    .gy-lg-0 {
        --mdb-gutter-y: 0
    }

    .g-lg-1,
    .gx-lg-1 {
        --mdb-gutter-x: 0.25rem
    }

    .g-lg-1,
    .gy-lg-1 {
        --mdb-gutter-y: 0.25rem
    }

    .g-lg-2,
    .gx-lg-2 {
        --mdb-gutter-x: 0.5rem
    }

    .g-lg-2,
    .gy-lg-2 {
        --mdb-gutter-y: 0.5rem
    }

    .g-lg-3,
    .gx-lg-3 {
        --mdb-gutter-x: 1rem
    }

    .g-lg-3,
    .gy-lg-3 {
        --mdb-gutter-y: 1rem
    }

    .g-lg-4,
    .gx-lg-4 {
        --mdb-gutter-x: 1.5rem
    }

    .g-lg-4,
    .gy-lg-4 {
        --mdb-gutter-y: 1.5rem
    }

    .g-lg-5,
    .gx-lg-5 {
        --mdb-gutter-x: 3rem
    }

    .g-lg-5,
    .gy-lg-5 {
        --mdb-gutter-y: 3rem
    }
}


@media(prefers-reduced-motion: reduce) {
    .form-control {
        transition: none
    }
}

.form-control[type=file] {
    overflow: hidden
}

.form-control[type=file]:not(:disabled):not([readonly]) {
    cursor: pointer
}

.form-control:focus {
    color: var(--mdb-surface-color);
    background-color: var(--mdb-body-bg);
    border-color: #3b71ca;
    outline: 0;
    box-shadow: var(--mdb-box-shadow-inset), 0 0 0 .25rem rgba(59, 113, 202, .25)
}

.form-control::-webkit-date-and-time-value {
    min-width: 85px;
    height: 1.6em;
    margin: 0
}

.form-control::-webkit-datetime-edit {
    display: block;
    padding: 0
}

.form-control::placeholder {
    color: rgba(var(--mdb-surface-color-rgb), 0.8);
    opacity: 1
}

.form-control:disabled {
    background-color: var(--mdb-secondary-bg);
    opacity: 1
}

.form-control::file-selector-button {
    padding: .375rem .75rem;
    margin: -0.375rem -0.75rem;
    margin-inline-end: .75rem;
    color: var(--mdb-surface-color);
    background-color: var(--mdb-tertiary-bg);
    pointer-events: none;
    border-color: inherit;
    border-style: solid;
    border-width: 0;
    border-inline-end-width: var(--mdb-border-width);
    border-radius: 0;
    transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out
}

@media(prefers-reduced-motion: reduce) {
    .form-control::file-selector-button {
        transition: none
    }
}

.form-control:hover:not(:disabled):not([readonly])::file-selector-button {
    background-color: var(--mdb-secondary-bg)
}

.form-control-plaintext {
    display: block;
    width: 100%;
    padding: .375rem 0;
    margin-bottom: 0;
    line-height: 1.6;
    color: var(--mdb-body-color);
    background-color: rgba(0, 0, 0, 0);
    border: solid rgba(0, 0, 0, 0);
    border-width: var(--mdb-border-width) 0
}

.form-control-plaintext:focus {
    outline: 0
}

.form-control-plaintext.form-control-sm,
.form-control-plaintext.form-control-lg {
    padding-right: 0;
    padding-left: 0
}

.form-control-sm {
    min-height: calc(1.6em + 0.5rem + calc(var(--mdb-border-width) * 2));
    padding: .25rem .5rem;
    font-size: 0.775rem;
    border-radius: var(--mdb-border-radius-sm)
}

.form-control-sm::file-selector-button {
    padding: .25rem .5rem;
    margin: -0.25rem -0.5rem;
    margin-inline-end: .5rem
}

.form-control-lg {
    min-height: calc(1.6em + 1rem + calc(var(--mdb-border-width) * 2));
    padding: .5rem 1rem;
    font-size: 1rem;
    border-radius: var(--mdb-border-radius-lg)
}

.form-control-lg::file-selector-button {
    padding: .5rem 1rem;
    margin: -0.5rem -1rem;
    margin-inline-end: 1rem
}

textarea.form-control {
    min-height: calc(1.6em + 0.75rem + calc(var(--mdb-border-width) * 2))
}

textarea.form-control-sm {
    min-height: calc(1.6em + 0.5rem + calc(var(--mdb-border-width) * 2))
}

textarea.form-control-lg {
    min-height: calc(1.6em + 1rem + calc(var(--mdb-border-width) * 2))
}

.form-control-color {
    width: 3rem;
    height: calc(1.6em + 0.75rem + calc(var(--mdb-border-width) * 2));
    padding: .375rem
}

.form-control-color:not(:disabled):not([readonly]) {
    cursor: pointer
}

.form-control-color::-moz-color-swatch {
    border: 0 !important;
    border-radius: var(--mdb-border-radius)
}

.form-control-color::-webkit-color-swatch {
    border: 0 !important;
    border-radius: var(--mdb-border-radius)
}

.form-control-color.form-control-sm {
    height: calc(1.6em + 0.5rem + calc(var(--mdb-border-width) * 2))
}

.form-control-color.form-control-lg {
    height: calc(1.6em + 1rem + calc(var(--mdb-border-width) * 2))
}

.form-select {
    --mdb-form-select-bg-img: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%234f4f4f' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='m2 5 6 6 6-6'/%3e%3c/svg%3e");
    display: block;
    width: 100%;
    padding: .375rem 2.25rem .375rem .75rem;
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.6;
    color: var(--mdb-surface-color);
    appearance: none;
    background-color: var(--mdb-body-bg);
    background-image: var(--mdb-form-select-bg-img), var(--mdb-form-select-bg-icon, none);
    background-repeat: no-repeat;
    background-position: right .75rem center;
    background-size: 16px 12px;
    border: var(--mdb-border-width) solid var(--mdb-border-color);
    border-radius: var(--mdb-border-radius);
    box-shadow: var(--mdb-box-shadow-inset);
    transition: all .2s linear
}

@media(prefers-reduced-motion: reduce) {
    .form-select {
        transition: none
    }
}

.form-select:focus {
    border-color: #3b71ca;
    outline: 0;
    box-shadow: var(--mdb-box-shadow-inset), 0 0 0 .25rem rgba(59, 113, 202, .25)
}

.form-select[multiple],
.form-select[size]:not([size="1"]) {
    padding-right: .75rem;
    background-image: none
}

.form-select:disabled {
    background-color: var(--mdb-secondary-bg)
}

.form-select:-moz-focusring {
    color: rgba(0, 0, 0, 0);
    text-shadow: 0 0 0 var(--mdb-surface-color)
}

.form-select-sm {
    padding-top: .25rem;
    padding-bottom: .25rem;
    padding-left: .5rem;
    font-size: 0.775rem;
    border-radius: var(--mdb-border-radius-sm)
}

.form-select-lg {
    padding-top: .5rem;
    padding-bottom: .5rem;
    padding-left: 1rem;
    font-size: 1rem;
    border-radius: var(--mdb-border-radius-lg)
}

[data-mdb-theme=dark] .form-select {
    --mdb-form-select-bg-img: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%23fff' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='m2 5 6 6 6-6'/%3e%3c/svg%3e")
}

.form-check {
    display: block;
    min-height: 1.6rem;
    padding-left: 1.5em;
    margin-bottom: .125rem
}

.form-check .form-check-input {
    float: left;
    margin-left: -1.5em
}

.form-check-reverse {
    padding-right: 1.5em;
    padding-left: 0;
    text-align: right
}

.form-check-reverse .form-check-input {
    float: right;
    margin-right: -1.5em;
    margin-left: 0
}

.form-check-input {
    --mdb-form-check-bg: var(--mdb-body-bg);
    flex-shrink: 0;
    width: 1em;
    height: 1em;
    margin-top: .3em;
    vertical-align: top;
    appearance: none;
    background-color: var(--mdb-form-check-bg);
    background-image: var(--mdb-form-check-bg-image);
    background-repeat: no-repeat;
    background-position: center;
    background-size: contain;
    border: var(--mdb-border-width) solid var(--mdb-border-color);
    print-color-adjust: exact
}

.form-check-input[type=checkbox] {
    border-radius: .25em
}

.form-check-input[type=radio] {
    border-radius: 50%
}

.form-check-input:active {
    filter: brightness(90%)
}

.form-check-input:focus {
    border-color: #3b71ca;
    outline: 0;
    box-shadow: 0 0 0 .25rem rgba(59, 113, 202, .25)
}

.form-check-input:checked {
    background-color: #3b71ca;
    border-color: #3b71ca
}

.form-check-input:checked[type=checkbox] {
    --mdb-form-check-bg-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3e%3cpath fill='none' stroke='%23fff' stroke-linecap='round' stroke-linejoin='round' stroke-width='3' d='m6 10 3 3 6-6'/%3e%3c/svg%3e")
}

.form-check-input:checked[type=radio] {
    --mdb-form-check-bg-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='2' fill='%23fff'/%3e%3c/svg%3e")
}

.form-check-input[type=checkbox]:indeterminate {
    background-color: #3b71ca;
    border-color: #757575;
    --mdb-form-check-bg-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3e%3cpath fill='none' stroke='%23fff' stroke-linecap='round' stroke-linejoin='round' stroke-width='3' d='M6 10h8'/%3e%3c/svg%3e")
}

.form-check-input:disabled {
    pointer-events: none;
    filter: none;
    opacity: .5
}

.form-check-input[disabled]~.form-check-label,
.form-check-input:disabled~.form-check-label {
    cursor: default;
    opacity: .5
}

.form-switch {
    padding-left: 2.5em
}

.form-switch .form-check-input {
    --mdb-form-switch-bg: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='rgba%280, 0, 0, 0.25%29'/%3e%3c/svg%3e");
    width: 2em;
    margin-left: -2.5em;
    background-image: var(--mdb-form-switch-bg);
    background-position: left center;
    border-radius: 2em;
    transition: background-position .15s ease-in-out
}

@media(prefers-reduced-motion: reduce) {
    .form-switch .form-check-input {
        transition: none
    }
}

.form-switch .form-check-input:focus {
    --mdb-form-switch-bg: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='%233b71ca'/%3e%3c/svg%3e")
}

.form-switch .form-check-input:checked {
    background-position: right center;
    --mdb-form-switch-bg: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='%23fff'/%3e%3c/svg%3e")
}

.form-switch.form-check-reverse {
    padding-right: 2.5em;
    padding-left: 0
}

.form-switch.form-check-reverse .form-check-input {
    margin-right: -2.5em;
    margin-left: 0
}

.form-check-inline {
    display: inline-block;
    margin-right: 1rem
}

.btn-check {
    position: absolute;
    clip: rect(0, 0, 0, 0);
    pointer-events: none
}

.btn-check[disabled]+.btn,
.btn-check:disabled+.btn {
    pointer-events: none;
    filter: none;
    opacity: .65
}

[data-mdb-theme=dark] .form-switch .form-check-input:not(:checked):not(:focus) {
    --mdb-form-switch-bg: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='rgba%28255, 255, 255, 0.25%29'/%3e%3c/svg%3e")
}

.form-range {
    width: 100%;
    height: 1.5rem;
    padding: 0;
    appearance: none;
    background-color: rgba(0, 0, 0, 0)
}

.form-range:focus {
    outline: 0
}

.form-range:focus::-webkit-slider-thumb {
    box-shadow: 0 0 0 1px #fff, 0 0 0 .25rem rgba(59, 113, 202, .25)
}

.form-range:focus::-moz-range-thumb {
    box-shadow: 0 0 0 1px #fff, 0 0 0 .25rem rgba(59, 113, 202, .25)
}

.form-range::-moz-focus-outer {
    border: 0
}

.form-range::-webkit-slider-thumb {
    width: 1rem;
    height: 1rem;
    margin-top: -0.25rem;
    appearance: none;
    background-color: #3b71ca;
    border: 0;
    border-radius: 1rem;
    box-shadow: 0 .1rem .25rem rgba(0, 0, 0, .1);
    transition: background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out
}

@media(prefers-reduced-motion: reduce) {
    .form-range::-webkit-slider-thumb {
        transition: none
    }
}

.form-range::-webkit-slider-thumb:active {
    background-color: #c4d4ef
}

.form-range::-webkit-slider-runnable-track {
    width: 100%;
    height: .5rem;
    color: rgba(0, 0, 0, 0);
    cursor: pointer;
    background-color: var(--mdb-secondary-bg);
    border-color: rgba(0, 0, 0, 0);
    border-radius: 1rem;
    box-shadow: var(--mdb-box-shadow-inset)
}

.form-range::-moz-range-thumb {
    width: 1rem;
    height: 1rem;
    appearance: none;
    background-color: #3b71ca;
    border: 0;
    border-radius: 1rem;
    box-shadow: 0 .1rem .25rem rgba(0, 0, 0, .1);
    transition: background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out
}

@media(prefers-reduced-motion: reduce) {
    .form-range::-moz-range-thumb {
        transition: none
    }
}

.form-range::-moz-range-thumb:active {
    background-color: #c4d4ef
}

.form-range::-moz-range-track {
    width: 100%;
    height: .5rem;
    color: rgba(0, 0, 0, 0);
    cursor: pointer;
    background-color: var(--mdb-secondary-bg);
    border-color: rgba(0, 0, 0, 0);
    border-radius: 1rem;
    box-shadow: var(--mdb-box-shadow-inset)
}

.form-range:disabled {
    pointer-events: none
}

.form-range:disabled::-webkit-slider-thumb {
    background-color: var(--mdb-form-control-disabled-bg)
}

.form-range:disabled::-moz-range-thumb {
    background-color: var(--mdb-form-control-disabled-bg)
}

.form-floating {
    position: relative
}

.form-floating>.form-control,
.form-floating>.form-control-plaintext,
.form-floating>.form-select {
    height: calc(3.5rem + calc(var(--mdb-border-width) * 2));
    min-height: calc(3.5rem + calc(var(--mdb-border-width) * 2));
    line-height: 1.25
}

.form-floating>label {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 2;
    height: 100%;
    padding: 1rem .75rem;
    overflow: hidden;
    text-align: start;
    text-overflow: ellipsis;
    white-space: nowrap;
    pointer-events: none;
    border: var(--mdb-border-width) solid rgba(0, 0, 0, 0);
    transform-origin: 0 0;
    transition: opacity .1s ease-in-out, transform .1s ease-in-out
}

@media(prefers-reduced-motion: reduce) {
    .form-floating>label {
        transition: none
    }
}

.form-floating>.form-control,
.form-floating>.form-control-plaintext {
    padding: 1rem .75rem
}

.form-floating>.form-control::placeholder,
.form-floating>.form-control-plaintext::placeholder {
    color: rgba(0, 0, 0, 0)
}

.form-floating>.form-control:focus,
.form-floating>.form-control:not(:placeholder-shown),
.form-floating>.form-control-plaintext:focus,
.form-floating>.form-control-plaintext:not(:placeholder-shown) {
    padding-top: 1.625rem;
    padding-bottom: .625rem
}

.form-floating>.form-control:-webkit-autofill,
.form-floating>.form-control-plaintext:-webkit-autofill {
    padding-top: 1.625rem;
    padding-bottom: .625rem
}

.form-floating>.form-select {
    padding-top: 1.625rem;
    padding-bottom: .625rem
}

.form-floating>.form-control:focus~label,
.form-floating>.form-control:not(:placeholder-shown)~label,
.form-floating>.form-control-plaintext~label,
.form-floating>.form-select~label {
    color: rgba(var(--mdb-body-color-rgb), 0.65);
    transform: scale(0.85) translateY(-0.5rem) translateX(0.15rem)
}

.form-floating>.form-control:focus~label::after,
.form-floating>.form-control:not(:placeholder-shown)~label::after,
.form-floating>.form-control-plaintext~label::after,
.form-floating>.form-select~label::after {
    position: absolute;
    inset: 1rem .375rem;
    z-index: -1;
    height: 1.5em;
    content: "";
    background-color: var(--mdb-body-bg);
    border-radius: var(--mdb-border-radius)
}

.form-floating>.form-control:-webkit-autofill~label {
    color: rgba(var(--mdb-body-color-rgb), 0.65);
    transform: scale(0.85) translateY(-0.5rem) translateX(0.15rem)
}

.form-floating>.form-control-plaintext~label {
    border-width: var(--mdb-border-width) 0
}

.form-floating>:disabled~label,
.form-floating>.form-control:disabled~label {
    color: #757575
}

.form-floating>:disabled~label::after,
.form-floating>.form-control:disabled~label::after {
    background-color: var(--mdb-secondary-bg)
}

.input-group {
    position: relative;
    display: flex;
    flex-wrap: wrap;
    align-items: stretch;
    width: 100%
}

.input-group>.form-control,
.input-group>.form-select,
.input-group>.form-floating {
    position: relative;
    flex: 1 1 auto;
    width: 1%;
    min-width: 0
}

.input-group>.form-control:focus,
.input-group>.form-select:focus,
.input-group>.form-floating:focus-within {
    z-index: 5
}

.input-group .btn {
    position: relative;
    z-index: 2
}

.input-group .btn:focus {
    z-index: 5
}

.input-group-text {
    display: flex;
    align-items: center;
    padding: .375rem .75rem;
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.6;
    color: var(--mdb-surface-color);
    text-align: center;
    white-space: nowrap;
    background-color: var(--mdb-tertiary-bg);
    border: var(--mdb-border-width) solid var(--mdb-border-color);
    border-radius: var(--mdb-border-radius)
}

.input-group-lg>.form-control,
.input-group-lg>.form-select,
.input-group-lg>.input-group-text,
.input-group-lg>.btn {
    padding: .5rem 1rem;
    font-size: 1rem;
    border-radius: var(--mdb-border-radius-lg)
}

.input-group-sm>.form-control,
.input-group-sm>.form-select,
.input-group-sm>.input-group-text,
.input-group-sm>.btn {
    padding: .25rem .5rem;
    font-size: 0.775rem;
    border-radius: var(--mdb-border-radius-sm)
}

.input-group-lg>.form-select,
.input-group-sm>.form-select {
    padding-right: 3rem
}

.input-group:not(.has-validation)>:not(:last-child):not(.dropdown-toggle):not(.dropdown-menu):not(.form-floating),
.input-group:not(.has-validation)>.dropdown-toggle:nth-last-child(n+3),
.input-group:not(.has-validation)>.form-floating:not(:last-child)>.form-control,
.input-group:not(.has-validation)>.form-floating:not(:last-child)>.form-select {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0
}

.input-group.has-validation>:nth-last-child(n+3):not(.dropdown-toggle):not(.dropdown-menu):not(.form-floating),
.input-group.has-validation>.dropdown-toggle:nth-last-child(n+4),
.input-group.has-validation>.form-floating:nth-last-child(n+3)>.form-control,
.input-group.has-validation>.form-floating:nth-last-child(n+3)>.form-select {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0
}

.input-group>:not(:first-child):not(.dropdown-menu):not(.valid-tooltip):not(.valid-feedback):not(.invalid-tooltip):not(.invalid-feedback) {
    margin-left: calc(var(--mdb-border-width)*-1);
    border-top-left-radius: 0;
    border-bottom-left-radius: 0
}

.input-group>.form-floating:not(:first-child)>.form-control,
.input-group>.form-floating:not(:first-child)>.form-select {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0
}

.valid-feedback {
    display: none;
    width: 100%;
    margin-top: .25rem;
    font-size: 0.875em;
    color: var(--mdb-form-valid-color)
}

.valid-tooltip {
    position: absolute;
    top: 100%;
    z-index: 5;
    display: none;
    max-width: 100%;
    padding: 6px 16px;
    margin-top: .1rem;
    font-size: 0.875rem;
    color: #fff;
    background-color: var(--mdb-success);
    border-radius: .25rem
}

.was-validated :valid~.valid-feedback,
.was-validated :valid~.valid-tooltip,
.is-valid~.valid-feedback,
.is-valid~.valid-tooltip {
    display: block
}

.was-validated .form-control:valid,
.form-control.is-valid {
    border-color: var(--mdb-form-valid-border-color);
    padding-right: calc(1.6em + 0.75rem);
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%2314a44d' d='M2.3 6.73.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z'/%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right calc(0.4em + 0.1875rem) center;
    background-size: calc(0.8em + 0.375rem) calc(0.8em + 0.375rem)
}

.was-validated .form-control:valid:focus,
.form-control.is-valid:focus {
    border-color: var(--mdb-form-valid-border-color);
    box-shadow: 0 0 0 .25rem rgba(var(--mdb-success-rgb), 0.25)
}

.was-validated textarea.form-control:valid,
textarea.form-control.is-valid {
    padding-right: calc(1.6em + 0.75rem);
    background-position: top calc(0.4em + 0.1875rem) right calc(0.4em + 0.1875rem)
}

.was-validated .form-select:valid,
.form-select.is-valid {
    border-color: var(--mdb-form-valid-border-color)
}

.was-validated .form-select:valid:not([multiple]):not([size]),
.was-validated .form-select:valid:not([multiple])[size="1"],
.form-select.is-valid:not([multiple]):not([size]),
.form-select.is-valid:not([multiple])[size="1"] {
    --mdb-form-select-bg-icon: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%2314a44d' d='M2.3 6.73.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z'/%3e%3c/svg%3e");
    padding-right: 4.125rem;
    background-position: right .75rem center, center right 2.25rem;
    background-size: 16px 12px, calc(0.8em + 0.375rem) calc(0.8em + 0.375rem)
}

.was-validated .form-select:valid:focus,
.form-select.is-valid:focus {
    border-color: var(--mdb-form-valid-border-color);
    box-shadow: 0 0 0 .25rem rgba(var(--mdb-success-rgb), 0.25)
}

.was-validated .form-control-color:valid,
.form-control-color.is-valid {
    width: calc(3rem + calc(1.6em + 0.75rem))
}

.was-validated .form-check-input:valid,
.form-check-input.is-valid {
    border-color: var(--mdb-form-valid-border-color)
}

.was-validated .form-check-input:valid:checked,
.form-check-input.is-valid:checked {
    background-color: var(--mdb-form-valid-color)
}

.was-validated .form-check-input:valid:focus,
.form-check-input.is-valid:focus {
    box-shadow: 0 0 0 .25rem rgba(var(--mdb-success-rgb), 0.25)
}

.was-validated .form-check-input:valid~.form-check-label,
.form-check-input.is-valid~.form-check-label {
    color: var(--mdb-form-valid-color)
}

.form-check-inline .form-check-input~.valid-feedback {
    margin-left: .5em
}

.was-validated .input-group>.form-control:not(:focus):valid,
.input-group>.form-control:not(:focus).is-valid,
.was-validated .input-group>.form-select:not(:focus):valid,
.input-group>.form-select:not(:focus).is-valid,
.was-validated .input-group>.form-floating:not(:focus-within):valid,
.input-group>.form-floating:not(:focus-within).is-valid {
    z-index: 3
}

.invalid-feedback {
    display: none;
    width: 100%;
    margin-top: .25rem;
    font-size: 0.875em;
    color: var(--mdb-form-invalid-color)
}

.invalid-tooltip {
    position: absolute;
    top: 100%;
    z-index: 5;
    display: none;
    max-width: 100%;
    padding: 6px 16px;
    margin-top: .1rem;
    font-size: 0.875rem;
    color: #fff;
    background-color: var(--mdb-danger);
    border-radius: .25rem
}

.was-validated :invalid~.invalid-feedback,
.was-validated :invalid~.invalid-tooltip,
.is-invalid~.invalid-feedback,
.is-invalid~.invalid-tooltip {
    display: block
}

.was-validated .form-control:invalid,
.form-control.is-invalid {
    border-color: var(--mdb-form-invalid-border-color);
    padding-right: calc(1.6em + 0.75rem);
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12' width='12' height='12' fill='none' stroke='%23dc4c64'%3e%3ccircle cx='6' cy='6' r='4.5'/%3e%3cpath stroke-linejoin='round' d='M5.8 3.6h.4L6 6.5z'/%3e%3ccircle cx='6' cy='8.2' r='.6' fill='%23dc4c64' stroke='none'/%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right calc(0.4em + 0.1875rem) center;
    background-size: calc(0.8em + 0.375rem) calc(0.8em + 0.375rem)
}

.was-validated .form-control:invalid:focus,
.form-control.is-invalid:focus {
    border-color: var(--mdb-form-invalid-border-color);
    box-shadow: 0 0 0 .25rem rgba(var(--mdb-danger-rgb), 0.25)
}

.was-validated textarea.form-control:invalid,
textarea.form-control.is-invalid {
    padding-right: calc(1.6em + 0.75rem);
    background-position: top calc(0.4em + 0.1875rem) right calc(0.4em + 0.1875rem)
}

.was-validated .form-select:invalid,
.form-select.is-invalid {
    border-color: var(--mdb-form-invalid-border-color)
}

.was-validated .form-select:invalid:not([multiple]):not([size]),
.was-validated .form-select:invalid:not([multiple])[size="1"],
.form-select.is-invalid:not([multiple]):not([size]),
.form-select.is-invalid:not([multiple])[size="1"] {
    --mdb-form-select-bg-icon: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12' width='12' height='12' fill='none' stroke='%23dc4c64'%3e%3ccircle cx='6' cy='6' r='4.5'/%3e%3cpath stroke-linejoin='round' d='M5.8 3.6h.4L6 6.5z'/%3e%3ccircle cx='6' cy='8.2' r='.6' fill='%23dc4c64' stroke='none'/%3e%3c/svg%3e");
    padding-right: 4.125rem;
    background-position: right .75rem center, center right 2.25rem;
    background-size: 16px 12px, calc(0.8em + 0.375rem) calc(0.8em + 0.375rem)
}

.was-validated .form-select:invalid:focus,
.form-select.is-invalid:focus {
    border-color: var(--mdb-form-invalid-border-color);
    box-shadow: 0 0 0 .25rem rgba(var(--mdb-danger-rgb), 0.25)
}

.was-validated .form-control-color:invalid,
.form-control-color.is-invalid {
    width: calc(3rem + calc(1.6em + 0.75rem))
}

.was-validated .form-check-input:invalid,
.form-check-input.is-invalid {
    border-color: var(--mdb-form-invalid-border-color)
}

.was-validated .form-check-input:invalid:checked,
.form-check-input.is-invalid:checked {
    background-color: var(--mdb-form-invalid-color)
}

.was-validated .form-check-input:invalid:focus,
.form-check-input.is-invalid:focus {
    box-shadow: 0 0 0 .25rem rgba(var(--mdb-danger-rgb), 0.25)
}

.was-validated .form-check-input:invalid~.form-check-label,
.form-check-input.is-invalid~.form-check-label {
    color: var(--mdb-form-invalid-color)
}

.form-check-inline .form-check-input~.invalid-feedback {
    margin-left: .5em
}

.was-validated .input-group>.form-control:not(:focus):invalid,
.input-group>.form-control:not(:focus).is-invalid,
.was-validated .input-group>.form-select:not(:focus):invalid,
.input-group>.form-select:not(:focus).is-invalid,
.was-validated .input-group>.form-floating:not(:focus-within):invalid,
.input-group>.form-floating:not(:focus-within).is-invalid {
    z-index: 4
}

.btn {
    --mdb-btn-padding-x: 1.5rem;
    --mdb-btn-padding-y: 0.375rem;
    --mdb-btn-font-family: ;
    --mdb-btn-font-size: 0.75rem;
    --mdb-btn-font-weight: 500;
    --mdb-btn-line-height: 1.5;
    --mdb-btn-color: var(--mdb-body-color);
    --mdb-btn-bg: transparent;
    --mdb-btn-border-width: 2px;
    --mdb-btn-border-color: transparent;
    --mdb-btn-border-radius: 0.25rem;
    --mdb-btn-hover-border-color: transparent;
    --mdb-btn-box-shadow: 0 4px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.35);
    --mdb-btn-disabled-opacity: 0.65;
    --mdb-btn-focus-box-shadow: 0 0 0 0.25rem rgba(var(--mdb-btn-focus-shadow-rgb), 0.5);
    display: inline-block;
    padding: var(--mdb-btn-padding-y) var(--mdb-btn-padding-x);
    font-family: var(--mdb-btn-font-family);
    font-size: var(--mdb-btn-font-size);
    font-weight: var(--mdb-btn-font-weight);
    line-height: var(--mdb-btn-line-height);
    color: var(--mdb-btn-color);
    text-align: center;
    vertical-align: middle;
    cursor: pointer;
    user-select: none;
    border: var(--mdb-btn-border-width) solid var(--mdb-btn-border-color);
    border-radius: var(--mdb-btn-border-radius);
    background-color: var(--mdb-btn-bg);
    box-shadow: var(--mdb-btn-box-shadow);
    transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out
}

@media(prefers-reduced-motion: reduce) {
    .btn {
        transition: none
    }
}

.btn:hover {
    color: var(--mdb-btn-hover-color);
    background-color: var(--mdb-btn-hover-bg);
    border-color: var(--mdb-btn-hover-border-color)
}

.btn-check+.btn:hover {
    color: var(--mdb-btn-color);
    background-color: var(--mdb-btn-bg);
    border-color: var(--mdb-btn-border-color)
}

.btn:focus-visible {
    color: var(--mdb-btn-hover-color);
    background-color: var(--mdb-btn-hover-bg);
    border-color: var(--mdb-btn-hover-border-color);
    outline: 0;
    box-shadow: var(--mdb-btn-box-shadow), var(--mdb-btn-focus-box-shadow)
}

.btn-check:focus-visible+.btn {
    border-color: var(--mdb-btn-hover-border-color);
    outline: 0;
    box-shadow: var(--mdb-btn-box-shadow), var(--mdb-btn-focus-box-shadow)
}

.btn-check:checked+.btn,
:not(.btn-check)+.btn:active,
.btn:first-child:active,
.btn.active,
.btn.show {
    color: var(--mdb-btn-active-color);
    background-color: var(--mdb-btn-active-bg);
    border-color: var(--mdb-btn-active-border-color);
    box-shadow: var(--mdb-btn-active-shadow)
}

.btn-check:checked+.btn:focus-visible,
:not(.btn-check)+.btn:active:focus-visible,
.btn:first-child:active:focus-visible,
.btn.active:focus-visible,
.btn.show:focus-visible {
    box-shadow: var(--mdb-btn-active-shadow), var(--mdb-btn-focus-box-shadow)
}

.btn:disabled,
.btn.disabled,
fieldset:disabled .btn {
    color: var(--mdb-btn-disabled-color);
    pointer-events: none;
    background-color: var(--mdb-btn-disabled-bg);
    border-color: var(--mdb-btn-disabled-border-color);
    opacity: var(--mdb-btn-disabled-opacity);
    box-shadow: none
}

.btn-primary {
    --mdb-btn-color: #fff;
    --mdb-btn-bg: #3b71ca;
    --mdb-btn-border-color: #3b71ca;
    --mdb-btn-hover-color: #fff;
    --mdb-btn-hover-bg: #386bc0;
    --mdb-btn-hover-border-color: #2f5aa2;
    --mdb-btn-focus-shadow-rgb: 88, 134, 210;
    --mdb-btn-active-color: #fff;
    --mdb-btn-active-bg: #3566b6;
    --mdb-btn-active-border-color: #2c5598;
    --mdb-btn-active-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-disabled-color: #fff;
    --mdb-btn-disabled-bg: #3b71ca;
    --mdb-btn-disabled-border-color: #3b71ca
}

.btn-secondary {
    --mdb-btn-color: #fff;
    --mdb-btn-bg: #9fa6b2;
    --mdb-btn-border-color: #9fa6b2;
    --mdb-btn-hover-color: #fff;
    --mdb-btn-hover-bg: #979ea9;
    --mdb-btn-hover-border-color: #7f858e;
    --mdb-btn-focus-shadow-rgb: 173, 179, 190;
    --mdb-btn-active-color: #fff;
    --mdb-btn-active-bg: #8f95a0;
    --mdb-btn-active-border-color: #777d86;
    --mdb-btn-active-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-disabled-color: #fff;
    --mdb-btn-disabled-bg: #9fa6b2;
    --mdb-btn-disabled-border-color: #9fa6b2
}

.btn-success {
    --mdb-btn-color: #fff;
    --mdb-btn-bg: #14a44d;
    --mdb-btn-border-color: #14a44d;
    --mdb-btn-hover-color: #fff;
    --mdb-btn-hover-bg: #139c49;
    --mdb-btn-hover-border-color: #10833e;
    --mdb-btn-focus-shadow-rgb: 55, 178, 104;
    --mdb-btn-active-color: #fff;
    --mdb-btn-active-bg: #129445;
    --mdb-btn-active-border-color: #0f7b3a;
    --mdb-btn-active-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-disabled-color: #fff;
    --mdb-btn-disabled-bg: #14a44d;
    --mdb-btn-disabled-border-color: #14a44d
}

.btn-danger {
    --mdb-btn-color: #fff;
    --mdb-btn-bg: #dc4c64;
    --mdb-btn-border-color: #dc4c64;
    --mdb-btn-hover-color: #fff;
    --mdb-btn-hover-bg: #d1485f;
    --mdb-btn-hover-border-color: #b03d50;
    --mdb-btn-focus-shadow-rgb: 225, 103, 123;
    --mdb-btn-active-color: #fff;
    --mdb-btn-active-bg: #c6445a;
    --mdb-btn-active-border-color: #a5394b;
    --mdb-btn-active-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-disabled-color: #fff;
    --mdb-btn-disabled-bg: #dc4c64;
    --mdb-btn-disabled-border-color: #dc4c64
}

.btn-warning {
    --mdb-btn-color: #fff;
    --mdb-btn-bg: #e4a11b;
    --mdb-btn-border-color: #e4a11b;
    --mdb-btn-hover-color: #fff;
    --mdb-btn-hover-bg: #d9991a;
    --mdb-btn-hover-border-color: #b68116;
    --mdb-btn-focus-shadow-rgb: 232, 175, 61;
    --mdb-btn-active-color: #fff;
    --mdb-btn-active-bg: #cd9118;
    --mdb-btn-active-border-color: #ab7914;
    --mdb-btn-active-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-disabled-color: #fff;
    --mdb-btn-disabled-bg: #e4a11b;
    --mdb-btn-disabled-border-color: #e4a11b
}

.btn-info {
    --mdb-btn-color: #fff;
    --mdb-btn-bg: #54b4d3;
    --mdb-btn-border-color: #54b4d3;
    --mdb-btn-hover-color: #fff;
    --mdb-btn-hover-bg: #50abc8;
    --mdb-btn-hover-border-color: #4390a9;
    --mdb-btn-focus-shadow-rgb: 110, 191, 218;
    --mdb-btn-active-color: #fff;
    --mdb-btn-active-bg: #4ca2be;
    --mdb-btn-active-border-color: #3f879e;
    --mdb-btn-active-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-disabled-color: #fff;
    --mdb-btn-disabled-bg: #54b4d3;
    --mdb-btn-disabled-border-color: #54b4d3
}

.btn-light {
    --mdb-btn-color: #000;
    --mdb-btn-bg: #fbfbfb;
    --mdb-btn-border-color: #fbfbfb;
    --mdb-btn-hover-color: #000;
    --mdb-btn-hover-bg: #eeeeee;
    --mdb-btn-hover-border-color: #c9c9c9;
    --mdb-btn-focus-shadow-rgb: 213, 213, 213;
    --mdb-btn-active-color: #000;
    --mdb-btn-active-bg: #e2e2e2;
    --mdb-btn-active-border-color: #bcbcbc;
    --mdb-btn-active-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-disabled-color: #000;
    --mdb-btn-disabled-bg: #fbfbfb;
    --mdb-btn-disabled-border-color: #fbfbfb
}

.btn-dark {
    --mdb-btn-color: #fff;
    --mdb-btn-bg: #332d2d;
    --mdb-btn-border-color: #332d2d;
    --mdb-btn-hover-color: #fff;
    --mdb-btn-hover-bg: #3d3838;
    --mdb-btn-hover-border-color: #474242;
    --mdb-btn-focus-shadow-rgb: 82, 77, 77;
    --mdb-btn-active-color: #fff;
    --mdb-btn-active-bg: #474242;
    --mdb-btn-active-border-color: #474242;
    --mdb-btn-active-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-disabled-color: #fff;
    --mdb-btn-disabled-bg: #332d2d;
    --mdb-btn-disabled-border-color: #332d2d
}

.btn-outline-primary {
    --mdb-btn-color: #3b71ca;
    --mdb-btn-border-color: #3b71ca;
    --mdb-btn-hover-color: #fff;
    --mdb-btn-hover-bg: #3b71ca;
    --mdb-btn-hover-border-color: #3b71ca;
    --mdb-btn-focus-shadow-rgb: 59, 113, 202;
    --mdb-btn-active-color: #fff;
    --mdb-btn-active-bg: #3b71ca;
    --mdb-btn-active-border-color: #3b71ca;
    --mdb-btn-active-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-disabled-color: #3b71ca;
    --mdb-btn-disabled-bg: transparent;
    --mdb-btn-disabled-border-color: #3b71ca;
    --mdb-gradient: none
}

.btn-outline-secondary {
    --mdb-btn-color: #9fa6b2;
    --mdb-btn-border-color: #9fa6b2;
    --mdb-btn-hover-color: #fff;
    --mdb-btn-hover-bg: #9fa6b2;
    --mdb-btn-hover-border-color: #9fa6b2;
    --mdb-btn-focus-shadow-rgb: 159, 166, 178;
    --mdb-btn-active-color: #fff;
    --mdb-btn-active-bg: #9fa6b2;
    --mdb-btn-active-border-color: #9fa6b2;
    --mdb-btn-active-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-disabled-color: #9fa6b2;
    --mdb-btn-disabled-bg: transparent;
    --mdb-btn-disabled-border-color: #9fa6b2;
    --mdb-gradient: none
}

.btn-outline-success {
    --mdb-btn-color: #14a44d;
    --mdb-btn-border-color: #14a44d;
    --mdb-btn-hover-color: #fff;
    --mdb-btn-hover-bg: #14a44d;
    --mdb-btn-hover-border-color: #14a44d;
    --mdb-btn-focus-shadow-rgb: 20, 164, 77;
    --mdb-btn-active-color: #fff;
    --mdb-btn-active-bg: #14a44d;
    --mdb-btn-active-border-color: #14a44d;
    --mdb-btn-active-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-disabled-color: #14a44d;
    --mdb-btn-disabled-bg: transparent;
    --mdb-btn-disabled-border-color: #14a44d;
    --mdb-gradient: none
}

.btn-outline-danger {
    --mdb-btn-color: #dc4c64;
    --mdb-btn-border-color: #dc4c64;
    --mdb-btn-hover-color: #fff;
    --mdb-btn-hover-bg: #dc4c64;
    --mdb-btn-hover-border-color: #dc4c64;
    --mdb-btn-focus-shadow-rgb: 220, 76, 100;
    --mdb-btn-active-color: #fff;
    --mdb-btn-active-bg: #dc4c64;
    --mdb-btn-active-border-color: #dc4c64;
    --mdb-btn-active-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-disabled-color: #dc4c64;
    --mdb-btn-disabled-bg: transparent;
    --mdb-btn-disabled-border-color: #dc4c64;
    --mdb-gradient: none
}

.btn-outline-warning {
    --mdb-btn-color: #e4a11b;
    --mdb-btn-border-color: #e4a11b;
    --mdb-btn-hover-color: #fff;
    --mdb-btn-hover-bg: #e4a11b;
    --mdb-btn-hover-border-color: #e4a11b;
    --mdb-btn-focus-shadow-rgb: 228, 161, 27;
    --mdb-btn-active-color: #fff;
    --mdb-btn-active-bg: #e4a11b;
    --mdb-btn-active-border-color: #e4a11b;
    --mdb-btn-active-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-disabled-color: #e4a11b;
    --mdb-btn-disabled-bg: transparent;
    --mdb-btn-disabled-border-color: #e4a11b;
    --mdb-gradient: none
}

.btn-outline-info {
    --mdb-btn-color: #54b4d3;
    --mdb-btn-border-color: #54b4d3;
    --mdb-btn-hover-color: #fff;
    --mdb-btn-hover-bg: #54b4d3;
    --mdb-btn-hover-border-color: #54b4d3;
    --mdb-btn-focus-shadow-rgb: 84, 180, 211;
    --mdb-btn-active-color: #fff;
    --mdb-btn-active-bg: #54b4d3;
    --mdb-btn-active-border-color: #54b4d3;
    --mdb-btn-active-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-disabled-color: #54b4d3;
    --mdb-btn-disabled-bg: transparent;
    --mdb-btn-disabled-border-color: #54b4d3;
    --mdb-gradient: none
}

.btn-outline-light {
    --mdb-btn-color: #fbfbfb;
    --mdb-btn-border-color: #fbfbfb;
    --mdb-btn-hover-color: #000;
    --mdb-btn-hover-bg: #fbfbfb;
    --mdb-btn-hover-border-color: #fbfbfb;
    --mdb-btn-focus-shadow-rgb: 251, 251, 251;
    --mdb-btn-active-color: #000;
    --mdb-btn-active-bg: #fbfbfb;
    --mdb-btn-active-border-color: #fbfbfb;
    --mdb-btn-active-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-disabled-color: #fbfbfb;
    --mdb-btn-disabled-bg: transparent;
    --mdb-btn-disabled-border-color: #fbfbfb;
    --mdb-gradient: none
}

.btn-outline-dark {
    --mdb-btn-color: #332d2d;
    --mdb-btn-border-color: #332d2d;
    --mdb-btn-hover-color: #fff;
    --mdb-btn-hover-bg: #332d2d;
    --mdb-btn-hover-border-color: #332d2d;
    --mdb-btn-focus-shadow-rgb: 51, 45, 45;
    --mdb-btn-active-color: #fff;
    --mdb-btn-active-bg: #332d2d;
    --mdb-btn-active-border-color: #332d2d;
    --mdb-btn-active-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-disabled-color: #332d2d;
    --mdb-btn-disabled-bg: transparent;
    --mdb-btn-disabled-border-color: #332d2d;
    --mdb-gradient: none
}

.btn-link {
    --mdb-btn-font-weight: 400;
    --mdb-btn-color: #3b71ca;
    --mdb-btn-bg: transparent;
    --mdb-btn-border-color: transparent;
    --mdb-btn-hover-color: #386bc0;
    --mdb-btn-hover-border-color: transparent;
    --mdb-btn-active-color: #386bc0;
    --mdb-btn-active-border-color: transparent;
    --mdb-btn-disabled-color: #9e9e9e;
    --mdb-btn-disabled-border-color: transparent;
    --mdb-btn-box-shadow: 0 0 0 #000;
    --mdb-btn-focus-shadow-rgb: 88, 134, 210;
    text-decoration: none
}

.btn-link:hover,
.btn-link:focus-visible {
    text-decoration: none
}

.btn-link:focus-visible {
    color: var(--mdb-btn-color)
}

.btn-link:hover {
    color: var(--mdb-btn-hover-color)
}

.btn-lg,
.btn-group-lg>.btn {
    --mdb-btn-padding-y: 0.5rem;
    --mdb-btn-padding-x: 1.6875rem;
    --mdb-btn-font-size: 0.875rem;
    --mdb-btn-border-radius: var(--mdb-border-radius-lg)
}

.btn-sm,
.btn-group-sm>.btn {
    --mdb-btn-padding-y: 0.25rem;
    --mdb-btn-padding-x: 1rem;
    --mdb-btn-font-size: 0.75rem;
    --mdb-btn-border-radius: var(--mdb-border-radius-sm)
}

.fade {
    transition: opacity .15s linear
}

@media(prefers-reduced-motion: reduce) {
    .fade {
        transition: none
    }
}

.fade:not(.show) {
    opacity: 0
}

.collapse:not(.show) {
    display: none
}

.collapsing {
    height: 0;
    overflow: hidden;
    transition: height .35s ease
}

@media(prefers-reduced-motion: reduce) {
    .collapsing {
        transition: none
    }
}

.collapsing.collapse-horizontal {
    width: 0;
    height: auto;
    transition: width .35s ease
}

@media(prefers-reduced-motion: reduce) {
    .collapsing.collapse-horizontal {
        transition: none
    }
}

.dropup,
.dropend,
.dropdown,
.dropstart,
.dropup-center,
.dropdown-center {
    position: relative
}

.dropdown-toggle {
    white-space: nowrap
}

.dropdown-toggle::after {
    display: inline-block;
    margin-left: .255em;
    vertical-align: .255em;
    content: "";
    border-top: .3em solid;
    border-right: .3em solid rgba(0, 0, 0, 0);
    border-bottom: 0;
    border-left: .3em solid rgba(0, 0, 0, 0)
}

.dropdown-toggle:empty::after {
    margin-left: 0
}

.dropdown-menu {
    --mdb-dropdown-zindex: 1000;
    --mdb-dropdown-min-width: 10rem;
    --mdb-dropdown-padding-x: 0;
    --mdb-dropdown-padding-y: 0.5rem;
    --mdb-dropdown-spacer: 0.125rem;
    --mdb-dropdown-font-size: 0.875rem;
    --mdb-dropdown-color: var(--mdb-surface-color);
    --mdb-dropdown-bg: var(--mdb-surface-bg);
    --mdb-dropdown-border-color: var(--mdb-border-color-translucent);
    --mdb-dropdown-border-radius: 0.5rem;
    --mdb-dropdown-border-width: var(--mdb-border-width);
    --mdb-dropdown-inner-border-radius: calc(0.5rem - var(--mdb-border-width));
    --mdb-dropdown-divider-bg: var(--mdb-divider-color);
    --mdb-dropdown-divider-margin-y: 0.5rem;
    --mdb-dropdown-box-shadow: 0 2px 15px -3px rgba(var(--mdb-box-shadow-color-rgb), 0.07), 0 10px 20px -2px rgba(var(--mdb-box-shadow-color-rgb), 0.04);
    --mdb-dropdown-link-color: var(--mdb-surface-color);
    --mdb-dropdown-link-hover-color: var(--mdb-surface-color);
    --mdb-dropdown-link-hover-bg: var(--mdb-tertiary-bg);
    --mdb-dropdown-link-active-color: #fff;
    --mdb-dropdown-link-active-bg: #3b71ca;
    --mdb-dropdown-link-disabled-color: rgba(var(--mdb-surface-color-rgb), 0.5);
    --mdb-dropdown-item-padding-x: 1rem;
    --mdb-dropdown-item-padding-y: 0.5rem;
    --mdb-dropdown-header-color: rgba(var(--mdb-emphasis-color-rgb), 0.55);
    --mdb-dropdown-header-padding-x: 1rem;
    --mdb-dropdown-header-padding-y: 0.5rem;
    position: absolute;
    z-index: var(--mdb-dropdown-zindex);
    display: none;
    min-width: var(--mdb-dropdown-min-width);
    padding: var(--mdb-dropdown-padding-y) var(--mdb-dropdown-padding-x);
    margin: 0;
    font-size: var(--mdb-dropdown-font-size);
    color: var(--mdb-dropdown-color);
    text-align: left;
    list-style: none;
    background-color: var(--mdb-dropdown-bg);
    background-clip: padding-box;
    border: var(--mdb-dropdown-border-width) solid var(--mdb-dropdown-border-color);
    border-radius: var(--mdb-dropdown-border-radius);
    box-shadow: var(--mdb-dropdown-box-shadow)
}

.dropdown-menu[data-mdb-popper] {
    top: 100%;
    left: 0;
    margin-top: var(--mdb-dropdown-spacer)
}

.dropdown-menu-start {
    --bs-position: start
}

.dropdown-menu-start[data-mdb-popper] {
    right: auto;
    left: 0
}

.dropdown-menu-end {
    --bs-position: end
}

.dropdown-menu-end[data-mdb-popper] {
    right: 0;
    left: auto
}

@media(min-width: 576px) {
    .dropdown-menu-sm-start {
        --bs-position: start
    }

    .dropdown-menu-sm-start[data-mdb-popper] {
        right: auto;
        left: 0
    }

    .dropdown-menu-sm-end {
        --bs-position: end
    }

    .dropdown-menu-sm-end[data-mdb-popper] {
        right: 0;
        left: auto
    }
}

@media(min-width: 768px) {
    .dropdown-menu-md-start {
        --bs-position: start
    }

    .dropdown-menu-md-start[data-mdb-popper] {
        right: auto;
        left: 0
    }

    .dropdown-menu-md-end {
        --bs-position: end
    }

    .dropdown-menu-md-end[data-mdb-popper] {
        right: 0;
        left: auto
    }
}

@media(min-width: 992px) {
    .dropdown-menu-lg-start {
        --bs-position: start
    }

    .dropdown-menu-lg-start[data-mdb-popper] {
        right: auto;
        left: 0
    }

    .dropdown-menu-lg-end {
        --bs-position: end
    }

    .dropdown-menu-lg-end[data-mdb-popper] {
        right: 0;
        left: auto
    }
}

@media(min-width: 1200px) {
    .dropdown-menu-xl-start {
        --bs-position: start
    }

    .dropdown-menu-xl-start[data-mdb-popper] {
        right: auto;
        left: 0
    }

    .dropdown-menu-xl-end {
        --bs-position: end
    }

    .dropdown-menu-xl-end[data-mdb-popper] {
        right: 0;
        left: auto
    }
}

@media(min-width: 1400px) {
    .dropdown-menu-xxl-start {
        --bs-position: start
    }

    .dropdown-menu-xxl-start[data-mdb-popper] {
        right: auto;
        left: 0
    }

    .dropdown-menu-xxl-end {
        --bs-position: end
    }

    .dropdown-menu-xxl-end[data-mdb-popper] {
        right: 0;
        left: auto
    }
}

.dropup .dropdown-menu[data-mdb-popper] {
    top: auto;
    bottom: 100%;
    margin-top: 0;
    margin-bottom: var(--mdb-dropdown-spacer)
}

.dropup .dropdown-toggle::after {
    display: inline-block;
    margin-left: .255em;
    vertical-align: .255em;
    content: "";
    border-top: 0;
    border-right: .3em solid rgba(0, 0, 0, 0);
    border-bottom: .3em solid;
    border-left: .3em solid rgba(0, 0, 0, 0)
}

.dropup .dropdown-toggle:empty::after {
    margin-left: 0
}

.dropend .dropdown-menu[data-mdb-popper] {
    top: 0;
    right: auto;
    left: 100%;
    margin-top: 0;
    margin-left: var(--mdb-dropdown-spacer)
}

.dropend .dropdown-toggle::after {
    display: inline-block;
    margin-left: .255em;
    vertical-align: .255em;
    content: "";
    border-top: .3em solid rgba(0, 0, 0, 0);
    border-right: 0;
    border-bottom: .3em solid rgba(0, 0, 0, 0);
    border-left: .3em solid
}

.dropend .dropdown-toggle:empty::after {
    margin-left: 0
}

.dropend .dropdown-toggle::after {
    vertical-align: 0
}

.dropstart .dropdown-menu[data-mdb-popper] {
    top: 0;
    right: 100%;
    left: auto;
    margin-top: 0;
    margin-right: var(--mdb-dropdown-spacer)
}

.dropstart .dropdown-toggle::after {
    display: inline-block;
    margin-left: .255em;
    vertical-align: .255em;
    content: ""
}

.dropstart .dropdown-toggle::after {
    display: none
}

.dropstart .dropdown-toggle::before {
    display: inline-block;
    margin-right: .255em;
    vertical-align: .255em;
    content: "";
    border-top: .3em solid rgba(0, 0, 0, 0);
    border-right: .3em solid;
    border-bottom: .3em solid rgba(0, 0, 0, 0)
}

.dropstart .dropdown-toggle:empty::after {
    margin-left: 0
}

.dropstart .dropdown-toggle::before {
    vertical-align: 0
}

.dropdown-divider {
    height: 0;
    margin: var(--mdb-dropdown-divider-margin-y) 0;
    overflow: hidden;
    border-top: 1px solid var(--mdb-dropdown-divider-bg);
    opacity: 1
}

.dropdown-item {
    display: block;
    width: 100%;
    padding: var(--mdb-dropdown-item-padding-y) var(--mdb-dropdown-item-padding-x);
    clear: both;
    font-weight: 400;
    color: var(--mdb-dropdown-link-color);
    text-align: inherit;
    white-space: nowrap;
    background-color: rgba(0, 0, 0, 0);
    border: 0;
    border-radius: var(--mdb-dropdown-item-border-radius, 0)
}

.dropdown-item:hover,
.dropdown-item:focus {
    color: var(--mdb-dropdown-link-hover-color);
    background-color: var(--mdb-dropdown-link-hover-bg)
}

.dropdown-item.active,
.dropdown-item:active {
    color: var(--mdb-dropdown-link-active-color);
    text-decoration: none;
    background-color: var(--mdb-dropdown-link-active-bg)
}

.dropdown-item.disabled,
.dropdown-item:disabled {
    color: var(--mdb-dropdown-link-disabled-color);
    pointer-events: none;
    background-color: rgba(0, 0, 0, 0)
}

.dropdown-menu.show {
    display: block
}

.dropdown-header {
    display: block;
    padding: var(--mdb-dropdown-header-padding-y) var(--mdb-dropdown-header-padding-x);
    margin-bottom: 0;
    font-size: 0.875rem;
    color: var(--mdb-dropdown-header-color);
    white-space: nowrap
}

.dropdown-item-text {
    display: block;
    padding: var(--mdb-dropdown-item-padding-y) var(--mdb-dropdown-item-padding-x);
    color: var(--mdb-dropdown-link-color)
}

.dropdown-menu-dark {
    --mdb-dropdown-color: #e0e0e0;
    --mdb-dropdown-bg: #4f4f4f;
    --mdb-dropdown-border-color: var(--mdb-border-color-translucent);
    --mdb-dropdown-box-shadow: ;
    --mdb-dropdown-link-color: #e0e0e0;
    --mdb-dropdown-link-hover-color: #fff;
    --mdb-dropdown-divider-bg: var(--mdb-divider-color);
    --mdb-dropdown-link-hover-bg: rgba(255, 255, 255, 0.15);
    --mdb-dropdown-link-active-color: #fff;
    --mdb-dropdown-link-active-bg: #3b71ca;
    --mdb-dropdown-link-disabled-color: #9e9e9e;
    --mdb-dropdown-header-color: #9e9e9e
}

.btn-group,
.btn-group-vertical {
    position: relative;
    display: inline-flex;
    vertical-align: middle
}

.btn-group>.btn,
.btn-group-vertical>.btn {
    position: relative;
    flex: 1 1 auto
}

.btn-group>.btn-check:checked+.btn,
.btn-group>.btn-check:focus+.btn,
.btn-group>.btn:hover,
.btn-group>.btn:focus,
.btn-group>.btn:active,
.btn-group>.btn.active,
.btn-group-vertical>.btn-check:checked+.btn,
.btn-group-vertical>.btn-check:focus+.btn,
.btn-group-vertical>.btn:hover,
.btn-group-vertical>.btn:focus,
.btn-group-vertical>.btn:active,
.btn-group-vertical>.btn.active {
    z-index: 1
}

.btn-toolbar {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start
}

.btn-toolbar .input-group {
    width: auto
}

.btn-group {
    border-radius: .25rem
}

.btn-group>:not(.btn-check:first-child)+.btn,
.btn-group>.btn-group:not(:first-child) {
    margin-left: calc(2px*-1)
}

.btn-group>.btn:not(:last-child):not(.dropdown-toggle),
.btn-group>.btn.dropdown-toggle-split:first-child,
.btn-group>.btn-group:not(:last-child)>.btn {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0
}

.btn-group>.btn:nth-child(n+3),
.btn-group>:not(.btn-check)+.btn,
.btn-group>.btn-group:not(:first-child)>.btn {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0
}

.dropdown-toggle-split {
    padding-right: 1.125rem;
    padding-left: 1.125rem
}

.dropdown-toggle-split::after,
.dropup .dropdown-toggle-split::after,
.dropend .dropdown-toggle-split::after {
    margin-left: 0
}

.dropstart .dropdown-toggle-split::before {
    margin-right: 0
}

.btn-sm+.dropdown-toggle-split,
.btn-group-sm>.btn+.dropdown-toggle-split {
    padding-right: .75rem;
    padding-left: .75rem
}

.btn-lg+.dropdown-toggle-split,
.btn-group-lg>.btn+.dropdown-toggle-split {
    padding-right: 1.265625rem;
    padding-left: 1.265625rem
}

.btn-group.show .dropdown-toggle {
    box-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1)
}

.btn-group.show .dropdown-toggle.btn-link {
    box-shadow: none
}

.btn-group-vertical {
    flex-direction: column;
    align-items: flex-start;
    justify-content: center
}

.btn-group-vertical>.btn,
.btn-group-vertical>.btn-group {
    width: 100%
}

.btn-group-vertical>.btn:not(:first-child),
.btn-group-vertical>.btn-group:not(:first-child) {
    margin-top: calc(2px*-1)
}

.btn-group-vertical>.btn:not(:last-child):not(.dropdown-toggle),
.btn-group-vertical>.btn-group:not(:last-child)>.btn {
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0
}

.btn-group-vertical>.btn~.btn,
.btn-group-vertical>.btn-group:not(:first-child)>.btn {
    border-top-left-radius: 0;
    border-top-right-radius: 0
}

.nav {
    --mdb-nav-link-padding-x: 1rem;
    --mdb-nav-link-padding-y: 0.5rem;
    --mdb-nav-link-font-weight: ;
    --mdb-nav-link-color: var(--mdb-link-color);
    --mdb-nav-link-hover-color: var(--mdb-link-hover-color);
    --mdb-nav-link-disabled-color: var(--mdb-secondary-color);
    display: flex;
    flex-wrap: wrap;
    padding-left: 0;
    margin-bottom: 0;
    list-style: none
}

.nav-link {
    display: block;
    padding: var(--mdb-nav-link-padding-y) var(--mdb-nav-link-padding-x);
    font-size: var(--mdb-nav-link-font-size);
    font-weight: var(--mdb-nav-link-font-weight);
    color: var(--mdb-nav-link-color);
    background: none;
    border: 0;
    transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out
}

@media(prefers-reduced-motion: reduce) {
    .nav-link {
        transition: none
    }
}

.nav-link:hover,
.nav-link:focus {
    color: var(--mdb-nav-link-hover-color)
}

.nav-link:focus-visible {
    outline: 0;
    box-shadow: 0 0 0 .25rem rgba(59, 113, 202, .25)
}

.nav-link.disabled,
.nav-link:disabled {
    color: var(--mdb-nav-link-disabled-color);
    pointer-events: none;
    cursor: default
}

.nav-tabs {
    --mdb-nav-tabs-border-width: var(--mdb-border-width);
    --mdb-nav-tabs-border-color: var(--mdb-border-color);
    --mdb-nav-tabs-border-radius: var(--mdb-border-radius);
    --mdb-nav-tabs-link-hover-border-color: var(--mdb-secondary-bg) var(--mdb-secondary-bg) var(--mdb-border-color);
    --mdb-nav-tabs-link-active-color: #3b71ca;
    --mdb-nav-tabs-link-active-bg: var(--mdb-body-bg);
    --mdb-nav-tabs-link-active-border-color: #3b71ca;
    border-bottom: var(--mdb-nav-tabs-border-width) solid var(--mdb-nav-tabs-border-color)
}

.nav-tabs .nav-link {
    margin-bottom: calc(-1*var(--mdb-nav-tabs-border-width));
    border: var(--mdb-nav-tabs-border-width) solid rgba(0, 0, 0, 0);
    border-top-left-radius: var(--mdb-nav-tabs-border-radius);
    border-top-right-radius: var(--mdb-nav-tabs-border-radius)
}

.nav-tabs .nav-link:hover,
.nav-tabs .nav-link:focus {
    isolation: isolate;
    border-color: var(--mdb-nav-tabs-link-hover-border-color)
}

.nav-tabs .nav-link.active,
.nav-tabs .nav-item.show .nav-link {
    color: var(--mdb-nav-tabs-link-active-color);
    background-color: var(--mdb-nav-tabs-link-active-bg);
    border-color: var(--mdb-nav-tabs-link-active-border-color)
}

.nav-tabs .dropdown-menu {
    margin-top: calc(-1*var(--mdb-nav-tabs-border-width));
    border-top-left-radius: 0;
    border-top-right-radius: 0
}

.nav-pills {
    --mdb-nav-pills-border-radius: var(--mdb-border-radius);
    --mdb-nav-pills-link-active-color: var(--mdb-primary-text-emphasis);
    --mdb-nav-pills-link-active-bg: var(--mdb-primary-bg-subtle)
}

.nav-pills .nav-link {
    border-radius: var(--mdb-nav-pills-border-radius)
}

.nav-pills .nav-link.active,
.nav-pills .show>.nav-link {
    color: var(--mdb-nav-pills-link-active-color);
    background-color: var(--mdb-nav-pills-link-active-bg)
}

.nav-underline {
    --mdb-nav-underline-gap: 1rem;
    --mdb-nav-underline-border-width: 0.125rem;
    --mdb-nav-underline-link-active-color: var(--mdb-emphasis-color);
    gap: var(--mdb-nav-underline-gap)
}

.nav-underline .nav-link {
    padding-right: 0;
    padding-left: 0;
    border-bottom: var(--mdb-nav-underline-border-width) solid rgba(0, 0, 0, 0)
}

.nav-underline .nav-link:hover,
.nav-underline .nav-link:focus {
    border-bottom-color: currentcolor
}

.nav-underline .nav-link.active,
.nav-underline .show>.nav-link {
    font-weight: 700;
    color: var(--mdb-nav-underline-link-active-color);
    border-bottom-color: currentcolor
}

.nav-fill>.nav-link,
.nav-fill .nav-item {
    flex: 1 1 auto;
    text-align: center
}

.nav-justified>.nav-link,
.nav-justified .nav-item {
    flex-basis: 0;
    flex-grow: 1;
    text-align: center
}

.nav-fill .nav-item .nav-link,
.nav-justified .nav-item .nav-link {
    width: 100%
}

.tab-content>.tab-pane {
    display: none
}

.tab-content>.active {
    display: block
}

.navbar {
    --mdb-navbar-padding-x: 0;
    --mdb-navbar-padding-y: 0.5rem;
    --mdb-navbar-color: rgba(var(--mdb-emphasis-color-rgb), 0.65);
    --mdb-navbar-hover-color: rgba(var(--mdb-emphasis-color-rgb), 0.8);
    --mdb-navbar-disabled-color: rgba(var(--mdb-emphasis-color-rgb), 0.3);
    --mdb-navbar-active-color: rgba(var(--mdb-emphasis-color-rgb), 1);
    --mdb-navbar-brand-padding-y: 0.3rem;
    --mdb-navbar-brand-margin-end: 1rem;
    --mdb-navbar-brand-font-size: 1.25rem;
    --mdb-navbar-brand-color: rgba(var(--mdb-emphasis-color-rgb), 1);
    --mdb-navbar-brand-hover-color: rgba(var(--mdb-emphasis-color-rgb), 1);
    --mdb-navbar-nav-link-padding-x: 0.5rem;
    --mdb-navbar-toggler-padding-y: 0.25rem;
    --mdb-navbar-toggler-padding-x: 0.75rem;
    --mdb-navbar-toggler-font-size: 1.25rem;
    --mdb-navbar-toggler-icon-bg: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%2879, 79, 79, 0.75%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");
    --mdb-navbar-toggler-border-color: rgba(var(--mdb-emphasis-color-rgb), 0.15);
    --mdb-navbar-toggler-border-radius: 0.25rem;
    --mdb-navbar-toggler-focus-width: 0.25rem;
    --mdb-navbar-toggler-transition: box-shadow 0.15s ease-in-out;
    position: relative;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    padding: var(--mdb-navbar-padding-y) var(--mdb-navbar-padding-x)
}

.navbar>.container,
.navbar>.container-fluid,
.navbar>.container-sm,
.navbar>.container-md,
.navbar>.container-lg,
.navbar>.container-xl,
.navbar>.container-xxl {
    display: flex;
    flex-wrap: inherit;
    align-items: center;
    justify-content: space-between
}

.navbar-brand {
    padding-top: var(--mdb-navbar-brand-padding-y);
    padding-bottom: var(--mdb-navbar-brand-padding-y);
    margin-right: var(--mdb-navbar-brand-margin-end);
    font-size: var(--mdb-navbar-brand-font-size);
    color: var(--mdb-navbar-brand-color);
    white-space: nowrap
}

.navbar-brand:hover,
.navbar-brand:focus {
    color: var(--mdb-navbar-brand-hover-color)
}

.navbar-nav {
    --mdb-nav-link-padding-x: 0;
    --mdb-nav-link-padding-y: 0.5rem;
    --mdb-nav-link-font-weight: ;
    --mdb-nav-link-color: var(--mdb-navbar-color);
    --mdb-nav-link-hover-color: var(--mdb-navbar-hover-color);
    --mdb-nav-link-disabled-color: var(--mdb-navbar-disabled-color);
    display: flex;
    flex-direction: column;
    padding-left: 0;
    margin-bottom: 0;
    list-style: none
}

.navbar-nav .nav-link.active,
.navbar-nav .nav-link.show {
    color: var(--mdb-navbar-active-color)
}

.navbar-nav .dropdown-menu {
    position: static
}

.navbar-text {
    padding-top: .5rem;
    padding-bottom: .5rem;
    color: var(--mdb-navbar-color)
}

.navbar-text a,
.navbar-text a:hover,
.navbar-text a:focus {
    color: var(--mdb-navbar-active-color)
}

.navbar-collapse {
    flex-basis: 100%;
    flex-grow: 1;
    align-items: center
}

.navbar-toggler {
    padding: var(--mdb-navbar-toggler-padding-y) var(--mdb-navbar-toggler-padding-x);
    font-size: var(--mdb-navbar-toggler-font-size);
    line-height: 1;
    color: var(--mdb-navbar-color);
    background-color: rgba(0, 0, 0, 0);
    border: var(--mdb-border-width) solid var(--mdb-navbar-toggler-border-color);
    border-radius: var(--mdb-navbar-toggler-border-radius);
    transition: var(--mdb-navbar-toggler-transition)
}

@media(prefers-reduced-motion: reduce) {
    .navbar-toggler {
        transition: none
    }
}

.navbar-toggler:hover {
    text-decoration: none
}

.navbar-toggler:focus {
    text-decoration: none;
    outline: 0;
    box-shadow: 0 0 0 var(--mdb-navbar-toggler-focus-width)
}

.navbar-toggler-icon {
    display: inline-block;
    width: 1.5em;
    height: 1.5em;
    vertical-align: middle;
    background-image: var(--mdb-navbar-toggler-icon-bg);
    background-repeat: no-repeat;
    background-position: center;
    background-size: 100%
}

.navbar-nav-scroll {
    max-height: var(--mdb-scroll-height, 75vh);
    overflow-y: auto
}

@media(min-width: 576px) {
    .navbar-expand-sm {
        flex-wrap: nowrap;
        justify-content: flex-start
    }

    .navbar-expand-sm .navbar-nav {
        flex-direction: row
    }

    .navbar-expand-sm .navbar-nav .dropdown-menu {
        position: absolute
    }

    .navbar-expand-sm .navbar-nav .nav-link {
        padding-right: var(--mdb-navbar-nav-link-padding-x);
        padding-left: var(--mdb-navbar-nav-link-padding-x)
    }

    .navbar-expand-sm .navbar-nav-scroll {
        overflow: visible
    }

    .navbar-expand-sm .navbar-collapse {
        display: flex !important;
        flex-basis: auto
    }

    .navbar-expand-sm .navbar-toggler {
        display: none
    }

    .navbar-expand-sm .offcanvas {
        position: static;
        z-index: auto;
        flex-grow: 1;
        width: auto !important;
        height: auto !important;
        visibility: visible !important;
        background-color: rgba(0, 0, 0, 0) !important;
        border: 0 !important;
        transform: none !important;
        box-shadow: none;
        transition: none
    }

    .navbar-expand-sm .offcanvas .offcanvas-header {
        display: none
    }

    .navbar-expand-sm .offcanvas .offcanvas-body {
        display: flex;
        flex-grow: 0;
        padding: 0;
        overflow-y: visible
    }
}

@media(min-width: 768px) {
    .navbar-expand-md {
        flex-wrap: nowrap;
        justify-content: flex-start
    }

    .navbar-expand-md .navbar-nav {
        flex-direction: row
    }

    .navbar-expand-md .navbar-nav .dropdown-menu {
        position: absolute
    }

    .navbar-expand-md .navbar-nav .nav-link {
        padding-right: var(--mdb-navbar-nav-link-padding-x);
        padding-left: var(--mdb-navbar-nav-link-padding-x)
    }

    .navbar-expand-md .navbar-nav-scroll {
        overflow: visible
    }

    .navbar-expand-md .navbar-collapse {
        display: flex !important;
        flex-basis: auto
    }

    .navbar-expand-md .navbar-toggler {
        display: none
    }

    .navbar-expand-md .offcanvas {
        position: static;
        z-index: auto;
        flex-grow: 1;
        width: auto !important;
        height: auto !important;
        visibility: visible !important;
        background-color: rgba(0, 0, 0, 0) !important;
        border: 0 !important;
        transform: none !important;
        box-shadow: none;
        transition: none
    }

    .navbar-expand-md .offcanvas .offcanvas-header {
        display: none
    }

    .navbar-expand-md .offcanvas .offcanvas-body {
        display: flex;
        flex-grow: 0;
        padding: 0;
        overflow-y: visible
    }
}

@media(min-width: 992px) {
    .navbar-expand-lg {
        flex-wrap: nowrap;
        justify-content: flex-start
    }

    .navbar-expand-lg .navbar-nav {
        flex-direction: row
    }

    .navbar-expand-lg .navbar-nav .dropdown-menu {
        position: absolute
    }

    .navbar-expand-lg .navbar-nav .nav-link {
        padding-right: var(--mdb-navbar-nav-link-padding-x);
        padding-left: var(--mdb-navbar-nav-link-padding-x)
    }

    .navbar-expand-lg .navbar-nav-scroll {
        overflow: visible
    }

    .navbar-expand-lg .navbar-collapse {
        display: flex !important;
        flex-basis: auto
    }

    .navbar-expand-lg .navbar-toggler {
        display: none
    }

    .navbar-expand-lg .offcanvas {
        position: static;
        z-index: auto;
        flex-grow: 1;
        width: auto !important;
        height: auto !important;
        visibility: visible !important;
        background-color: rgba(0, 0, 0, 0) !important;
        border: 0 !important;
        transform: none !important;
        box-shadow: none;
        transition: none
    }

    .navbar-expand-lg .offcanvas .offcanvas-header {
        display: none
    }

    .navbar-expand-lg .offcanvas .offcanvas-body {
        display: flex;
        flex-grow: 0;
        padding: 0;
        overflow-y: visible
    }
}

@media(min-width: 1200px) {
    .navbar-expand-xl {
        flex-wrap: nowrap;
        justify-content: flex-start
    }

    .navbar-expand-xl .navbar-nav {
        flex-direction: row
    }

    .navbar-expand-xl .navbar-nav .dropdown-menu {
        position: absolute
    }

    .navbar-expand-xl .navbar-nav .nav-link {
        padding-right: var(--mdb-navbar-nav-link-padding-x);
        padding-left: var(--mdb-navbar-nav-link-padding-x)
    }

    .navbar-expand-xl .navbar-nav-scroll {
        overflow: visible
    }

    .navbar-expand-xl .navbar-collapse {
        display: flex !important;
        flex-basis: auto
    }

    .navbar-expand-xl .navbar-toggler {
        display: none
    }

    .navbar-expand-xl .offcanvas {
        position: static;
        z-index: auto;
        flex-grow: 1;
        width: auto !important;
        height: auto !important;
        visibility: visible !important;
        background-color: rgba(0, 0, 0, 0) !important;
        border: 0 !important;
        transform: none !important;
        box-shadow: none;
        transition: none
    }

    .navbar-expand-xl .offcanvas .offcanvas-header {
        display: none
    }

    .navbar-expand-xl .offcanvas .offcanvas-body {
        display: flex;
        flex-grow: 0;
        padding: 0;
        overflow-y: visible
    }
}

@media(min-width: 1400px) {
    .navbar-expand-xxl {
        flex-wrap: nowrap;
        justify-content: flex-start
    }

    .navbar-expand-xxl .navbar-nav {
        flex-direction: row
    }

    .navbar-expand-xxl .navbar-nav .dropdown-menu {
        position: absolute
    }

    .navbar-expand-xxl .navbar-nav .nav-link {
        padding-right: var(--mdb-navbar-nav-link-padding-x);
        padding-left: var(--mdb-navbar-nav-link-padding-x)
    }

    .navbar-expand-xxl .navbar-nav-scroll {
        overflow: visible
    }

    .navbar-expand-xxl .navbar-collapse {
        display: flex !important;
        flex-basis: auto
    }

    .navbar-expand-xxl .navbar-toggler {
        display: none
    }

    .navbar-expand-xxl .offcanvas {
        position: static;
        z-index: auto;
        flex-grow: 1;
        width: auto !important;
        height: auto !important;
        visibility: visible !important;
        background-color: rgba(0, 0, 0, 0) !important;
        border: 0 !important;
        transform: none !important;
        box-shadow: none;
        transition: none
    }

    .navbar-expand-xxl .offcanvas .offcanvas-header {
        display: none
    }

    .navbar-expand-xxl .offcanvas .offcanvas-body {
        display: flex;
        flex-grow: 0;
        padding: 0;
        overflow-y: visible
    }
}

.navbar-expand {
    flex-wrap: nowrap;
    justify-content: flex-start
}

.navbar-expand .navbar-nav {
    flex-direction: row
}

.navbar-expand .navbar-nav .dropdown-menu {
    position: absolute
}

.navbar-expand .navbar-nav .nav-link {
    padding-right: var(--mdb-navbar-nav-link-padding-x);
    padding-left: var(--mdb-navbar-nav-link-padding-x)
}

.navbar-expand .navbar-nav-scroll {
    overflow: visible
}

.navbar-expand .navbar-collapse {
    display: flex !important;
    flex-basis: auto
}

.navbar-expand .navbar-toggler {
    display: none
}

.navbar-expand .offcanvas {
    position: static;
    z-index: auto;
    flex-grow: 1;
    width: auto !important;
    height: auto !important;
    visibility: visible !important;
    background-color: rgba(0, 0, 0, 0) !important;
    border: 0 !important;
    transform: none !important;
    box-shadow: none;
    transition: none
}

.navbar-expand .offcanvas .offcanvas-header {
    display: none
}

.navbar-expand .offcanvas .offcanvas-body {
    display: flex;
    flex-grow: 0;
    padding: 0;
    overflow-y: visible
}

.navbar-dark,
.navbar[data-mdb-theme=dark] {
    --mdb-navbar-color: rgba(255, 255, 255, 0.55);
    --mdb-navbar-hover-color: rgba(255, 255, 255, 0.75);
    --mdb-navbar-disabled-color: rgba(255, 255, 255, 0.25);
    --mdb-navbar-active-color: #fff;
    --mdb-navbar-brand-color: #fff;
    --mdb-navbar-brand-hover-color: #fff;
    --mdb-navbar-toggler-border-color: rgba(255, 255, 255, 0.1);
    --mdb-navbar-toggler-icon-bg: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%28255, 255, 255, 0.55%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e")
}

[data-mdb-theme=dark] .navbar-toggler-icon {
    --mdb-navbar-toggler-icon-bg: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%28255, 255, 255, 0.55%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e")
}

.card {
    --mdb-card-spacer-y: 1.5rem;
    --mdb-card-spacer-x: 1.5rem;
    --mdb-card-title-spacer-y: 0.5rem;
    --mdb-card-title-color: ;
    --mdb-card-subtitle-color: ;
    --mdb-card-border-width: var(--mdb-border-width);
    --mdb-card-border-color: rgba(0, 0, 0, 0.175);
    --mdb-card-border-radius: 0.5rem;
    --mdb-card-box-shadow: 0 2px 15px -3px rgba(var(--mdb-box-shadow-color-rgb), 0.07), 0 10px 20px -2px rgba(var(--mdb-box-shadow-color-rgb), 0.04);
    --mdb-card-inner-border-radius: calc(0.5rem - (var(--mdb-border-width)));
    --mdb-card-cap-padding-y: 0.75rem;
    --mdb-card-cap-padding-x: 1.5rem;
    --mdb-card-cap-bg: rgba(255, 255, 255, 0);
    --mdb-card-cap-color: ;
    --mdb-card-height: ;
    --mdb-card-color: ;
    --mdb-card-bg: var(--mdb-surface-bg);
    --mdb-card-img-overlay-padding: 1.5rem;
    --mdb-card-group-margin: 0.75rem;
    position: relative;
    display: flex;
    flex-direction: column;
    min-width: 0;
    height: var(--mdb-card-height);
    color: var(--mdb-body-color);
    word-wrap: break-word;
    background-color: var(--mdb-card-bg);
    background-clip: border-box;
    border: var(--mdb-card-border-width) solid var(--mdb-card-border-color);
    border-radius: var(--mdb-card-border-radius);
    box-shadow: var(--mdb-card-box-shadow)
}

.card>hr {
    margin-right: 0;
    margin-left: 0
}

.card>.list-group {
    border-top: inherit;
    border-bottom: inherit
}

.card>.list-group:first-child {
    border-top-width: 0;
    border-top-left-radius: var(--mdb-card-inner-border-radius);
    border-top-right-radius: var(--mdb-card-inner-border-radius)
}

.card>.list-group:last-child {
    border-bottom-width: 0;
    border-bottom-right-radius: var(--mdb-card-inner-border-radius);
    border-bottom-left-radius: var(--mdb-card-inner-border-radius)
}

.card>.card-header+.list-group,
.card>.list-group+.card-footer {
    border-top: 0
}

.card-body {
    flex: 1 1 auto;
    padding: var(--mdb-card-spacer-y) var(--mdb-card-spacer-x);
    color: var(--mdb-card-color)
}

.card-title {
    margin-bottom: var(--mdb-card-title-spacer-y);
    color: var(--mdb-card-title-color)
}

.card-subtitle {
    margin-top: calc(-0.5*var(--mdb-card-title-spacer-y));
    margin-bottom: 0;
    color: var(--mdb-card-subtitle-color)
}

.card-text:last-child {
    margin-bottom: 0
}

.card-link+.card-link {
    margin-left: var(--mdb-card-spacer-x)
}

.card-header {
    padding: var(--mdb-card-cap-padding-y) var(--mdb-card-cap-padding-x);
    margin-bottom: 0;
    color: var(--mdb-card-cap-color);
    background-color: var(--mdb-card-cap-bg);
    border-bottom: var(--mdb-card-border-width) solid var(--mdb-card-border-color)
}

.card-header:first-child {
    border-radius: var(--mdb-card-inner-border-radius) var(--mdb-card-inner-border-radius) 0 0
}

.card-footer {
    padding: var(--mdb-card-cap-padding-y) var(--mdb-card-cap-padding-x);
    color: var(--mdb-card-cap-color);
    background-color: var(--mdb-card-cap-bg);
    border-top: var(--mdb-card-border-width) solid var(--mdb-card-border-color)
}

.card-footer:last-child {
    border-radius: 0 0 var(--mdb-card-inner-border-radius) var(--mdb-card-inner-border-radius)
}

.card-header-tabs {
    margin-right: calc(-0.5*var(--mdb-card-cap-padding-x));
    margin-bottom: calc(-1*var(--mdb-card-cap-padding-y));
    margin-left: calc(-0.5*var(--mdb-card-cap-padding-x));
    border-bottom: 0
}

.card-header-tabs .nav-link.active {
    background-color: var(--mdb-card-bg);
    border-bottom-color: var(--mdb-card-bg)
}

.card-header-pills {
    margin-right: calc(-0.5*var(--mdb-card-cap-padding-x));
    margin-left: calc(-0.5*var(--mdb-card-cap-padding-x))
}

.card-img-overlay {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    padding: var(--mdb-card-img-overlay-padding);
    border-radius: var(--mdb-card-inner-border-radius)
}

.card-img,
.card-img-top,
.card-img-bottom {
    width: 100%
}

.card-img,
.card-img-top {
    border-top-left-radius: var(--mdb-card-inner-border-radius);
    border-top-right-radius: var(--mdb-card-inner-border-radius)
}

.card-img,
.card-img-bottom {
    border-bottom-right-radius: var(--mdb-card-inner-border-radius);
    border-bottom-left-radius: var(--mdb-card-inner-border-radius)
}

.card-group>.card {
    margin-bottom: var(--mdb-card-group-margin)
}

@media(min-width: 576px) {
    .card-group {
        display: flex;
        flex-flow: row wrap
    }

    .card-group>.card {
        flex: 1 0 0%;
        margin-bottom: 0
    }

    .card-group>.card+.card {
        margin-left: 0;
        border-left: 0
    }

    .card-group>.card:not(:last-child) {
        border-top-right-radius: 0;
        border-bottom-right-radius: 0
    }

    .card-group>.card:not(:last-child) .card-img-top,
    .card-group>.card:not(:last-child) .card-header {
        border-top-right-radius: 0
    }

    .card-group>.card:not(:last-child) .card-img-bottom,
    .card-group>.card:not(:last-child) .card-footer {
        border-bottom-right-radius: 0
    }

    .card-group>.card:not(:first-child) {
        border-top-left-radius: 0;
        border-bottom-left-radius: 0
    }

    .card-group>.card:not(:first-child) .card-img-top,
    .card-group>.card:not(:first-child) .card-header {
        border-top-left-radius: 0
    }

    .card-group>.card:not(:first-child) .card-img-bottom,
    .card-group>.card:not(:first-child) .card-footer {
        border-bottom-left-radius: 0
    }
}

.breadcrumb {
    --mdb-breadcrumb-padding-x: 0;
    --mdb-breadcrumb-padding-y: 0;
    --mdb-breadcrumb-margin-bottom: 1rem;
    --mdb-breadcrumb-bg: ;
    --mdb-breadcrumb-border-radius: ;
    --mdb-breadcrumb-divider-color: rgba(var(--mdb-emphasis-color-rgb), 0.55);
    --mdb-breadcrumb-item-padding-x: 0.5rem;
    --mdb-breadcrumb-item-active-color: rgba(var(--mdb-emphasis-color-rgb), 0.55);
    display: flex;
    flex-wrap: wrap;
    padding: var(--mdb-breadcrumb-padding-y) var(--mdb-breadcrumb-padding-x);
    margin-bottom: var(--mdb-breadcrumb-margin-bottom);
    font-size: var(--mdb-breadcrumb-font-size);
    list-style: none;
    background-color: var(--mdb-breadcrumb-bg);
    border-radius: var(--mdb-breadcrumb-border-radius)
}

.breadcrumb-item+.breadcrumb-item {
    padding-left: var(--mdb-breadcrumb-item-padding-x)
}

.breadcrumb-item+.breadcrumb-item::before {
    float: left;
    padding-right: var(--mdb-breadcrumb-item-padding-x);
    color: var(--mdb-breadcrumb-divider-color);
    content: var(--mdb-breadcrumb-divider, "/")
        /* rtl: var(--mdb-breadcrumb-divider, "/") */
}

.breadcrumb-item.active {
    color: var(--mdb-breadcrumb-item-active-color)
}

.pagination {
    --mdb-pagination-padding-x: 0.75rem;
    --mdb-pagination-padding-y: 0.375rem;
    --mdb-pagination-font-size: 0.9rem;
    --mdb-pagination-color: var(--mdb-body-color);
    --mdb-pagination-bg: var(--mdb-body-bg);
    --mdb-pagination-border-width: var(--mdb-border-width);
    --mdb-pagination-border-color: var(--mdb-border-color);
    --mdb-pagination-border-radius: 0.25rem;
    --mdb-pagination-hover-color: var(--mdb-body-color);
    --mdb-pagination-hover-bg: var(--mdb-highlight-bg-color);
    --mdb-pagination-hover-border-color: var(--mdb-border-color);
    --mdb-pagination-focus-color: var(--mdb-link-hover-color);
    --mdb-pagination-focus-bg: var(--mdb-highlight-bg-color);
    --mdb-pagination-focus-box-shadow: 0 0 0 0.25rem rgba(59, 113, 202, 0.25);
    --mdb-pagination-active-color: var(--mdb-primary-text-emphasis);
    --mdb-pagination-active-bg: var(--mdb-primary-bg-subtle);
    --mdb-pagination-active-border-color: #3b71ca;
    --mdb-pagination-disabled-color: rgba(var(--mdb-body-color-rgb), 0.55);
    --mdb-pagination-disabled-bg: transparent;
    --mdb-pagination-disabled-border-color: var(--mdb-border-color);
    display: flex;
    padding-left: 0;
    list-style: none
}

.page-link {
    position: relative;
    display: block;
    padding: var(--mdb-pagination-padding-y) var(--mdb-pagination-padding-x);
    font-size: var(--mdb-pagination-font-size);
    color: var(--mdb-pagination-color);
    background-color: var(--mdb-pagination-bg);
    border: var(--mdb-pagination-border-width) solid var(--mdb-pagination-border-color);
    transition: all .3s linear
}

@media(prefers-reduced-motion: reduce) {
    .page-link {
        transition: none
    }
}

.page-link:hover {
    z-index: 2;
    color: var(--mdb-pagination-hover-color);
    background-color: var(--mdb-pagination-hover-bg);
    border-color: var(--mdb-pagination-hover-border-color)
}

.page-link:focus {
    z-index: 3;
    color: var(--mdb-pagination-focus-color);
    background-color: var(--mdb-pagination-focus-bg);
    outline: 0;
    box-shadow: var(--mdb-pagination-focus-box-shadow)
}

.page-link.active,
.active>.page-link {
    z-index: 3;
    color: var(--mdb-pagination-active-color);
    background-color: var(--mdb-pagination-active-bg);
    border-color: var(--mdb-pagination-active-border-color)
}

.page-link.disabled,
.disabled>.page-link {
    color: var(--mdb-pagination-disabled-color);
    pointer-events: none;
    background-color: var(--mdb-pagination-disabled-bg);
    border-color: var(--mdb-pagination-disabled-border-color)
}

.page-item:not(:first-child) .page-link {
    margin-left: calc(var(--mdb-border-width)*-1)
}

.page-item:first-child .page-link {
    border-top-left-radius: var(--mdb-pagination-border-radius);
    border-bottom-left-radius: var(--mdb-pagination-border-radius)
}

.page-item:last-child .page-link {
    border-top-right-radius: var(--mdb-pagination-border-radius);
    border-bottom-right-radius: var(--mdb-pagination-border-radius)
}

.pagination-lg {
    --mdb-pagination-padding-x: 1.5rem;
    --mdb-pagination-padding-y: 0.75rem;
    --mdb-pagination-font-size: 1.25rem;
    --mdb-pagination-border-radius: var(--mdb-border-radius-lg)
}

.pagination-sm {
    --mdb-pagination-padding-x: 0.5rem;
    --mdb-pagination-padding-y: 0.25rem;
    --mdb-pagination-font-size: 0.875rem;
    --mdb-pagination-border-radius: var(--mdb-border-radius-sm)
}

.badge {
    --mdb-badge-padding-x: 0.65em;
    --mdb-badge-padding-y: 0.35em;
    --mdb-badge-font-size: 0.75em;
    --mdb-badge-font-weight: 700;
    --mdb-badge-color: #fff;
    --mdb-badge-border-radius: 0.27rem;
    display: inline-block;
    padding: var(--mdb-badge-padding-y) var(--mdb-badge-padding-x);
    font-size: var(--mdb-badge-font-size);
    font-weight: var(--mdb-badge-font-weight);
    line-height: 1;
    color: var(--mdb-badge-color);
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: var(--mdb-badge-border-radius)
}

.badge:empty {
    display: none
}

.btn .badge {
    position: relative;
    top: -1px
}

.alert {
    --mdb-alert-bg: transparent;
    --mdb-alert-padding-x: 1.5rem;
    --mdb-alert-padding-y: 1.25rem;
    --mdb-alert-margin-bottom: 1rem;
    --mdb-alert-color: inherit;
    --mdb-alert-border-color: transparent;
    --mdb-alert-border: var(--mdb-border-width) solid var(--mdb-alert-border-color);
    --mdb-alert-border-radius: 0.5rem;
    --mdb-alert-link-color: inherit;
    position: relative;
    padding: var(--mdb-alert-padding-y) var(--mdb-alert-padding-x);
    margin-bottom: var(--mdb-alert-margin-bottom);
    color: var(--mdb-alert-color);
    background-color: var(--mdb-alert-bg);
    border: var(--mdb-alert-border);
    border-radius: var(--mdb-alert-border-radius)
}

.alert-heading {
    color: inherit
}

.alert-link {
    font-weight: 700;
    color: var(--mdb-alert-link-color)
}

.alert-dismissible {
    padding-right: 4.5rem
}

.alert-dismissible .btn-close {
    position: absolute;
    top: 0;
    right: 0;
    z-index: 2;
    padding: 1.5625rem 1.5rem
}

.alert-primary {
    --mdb-alert-color: var(--mdb-primary-text-emphasis);
    --mdb-alert-bg: var(--mdb-primary-bg-subtle);
    --mdb-alert-border-color: var(--mdb-primary-border-subtle);
    --mdb-alert-link-color: var(--mdb-primary-text-emphasis)
}

.alert-secondary {
    --mdb-alert-color: var(--mdb-secondary-text-emphasis);
    --mdb-alert-bg: var(--mdb-secondary-bg-subtle);
    --mdb-alert-border-color: var(--mdb-secondary-border-subtle);
    --mdb-alert-link-color: var(--mdb-secondary-text-emphasis)
}

.alert-success {
    --mdb-alert-color: var(--mdb-success-text-emphasis);
    --mdb-alert-bg: var(--mdb-success-bg-subtle);
    --mdb-alert-border-color: var(--mdb-success-border-subtle);
    --mdb-alert-link-color: var(--mdb-success-text-emphasis)
}

.alert-danger {
    --mdb-alert-color: var(--mdb-danger-text-emphasis);
    --mdb-alert-bg: var(--mdb-danger-bg-subtle);
    --mdb-alert-border-color: var(--mdb-danger-border-subtle);
    --mdb-alert-link-color: var(--mdb-danger-text-emphasis)
}

.alert-warning {
    --mdb-alert-color: var(--mdb-warning-text-emphasis);
    --mdb-alert-bg: var(--mdb-warning-bg-subtle);
    --mdb-alert-border-color: var(--mdb-warning-border-subtle);
    --mdb-alert-link-color: var(--mdb-warning-text-emphasis)
}

.alert-info {
    --mdb-alert-color: var(--mdb-info-text-emphasis);
    --mdb-alert-bg: var(--mdb-info-bg-subtle);
    --mdb-alert-border-color: var(--mdb-info-border-subtle);
    --mdb-alert-link-color: var(--mdb-info-text-emphasis)
}

.alert-light {
    --mdb-alert-color: var(--mdb-light-text-emphasis);
    --mdb-alert-bg: var(--mdb-light-bg-subtle);
    --mdb-alert-border-color: var(--mdb-light-border-subtle);
    --mdb-alert-link-color: var(--mdb-light-text-emphasis)
}

.alert-dark {
    --mdb-alert-color: var(--mdb-dark-text-emphasis);
    --mdb-alert-bg: var(--mdb-dark-bg-subtle);
    --mdb-alert-border-color: var(--mdb-dark-border-subtle);
    --mdb-alert-link-color: var(--mdb-dark-text-emphasis)
}

.accordion {
    --mdb-accordion-color: var(--mdb-surface-color);
    --mdb-accordion-bg: var(--mdb-body-bg);
    --mdb-accordion-transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out, border-radius 0.15s ease;
    --mdb-accordion-border-color: var(--mdb-border-color);
    --mdb-accordion-border-width: var(--mdb-border-width);
    --mdb-accordion-border-radius: 0.5rem;
    --mdb-accordion-inner-border-radius: calc(0.5rem - (var(--mdb-border-width)));
    --mdb-accordion-btn-padding-x: 1.5rem;
    --mdb-accordion-btn-padding-y: 1.15rem;
    --mdb-accordion-btn-color: var(--mdb-surface-color);
    --mdb-accordion-btn-bg: var(--mdb-accordion-bg);
    --mdb-accordion-btn-icon: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='var%28--mdb-surface-color%29'%3e%3cpath fill-rule='evenodd' d='M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z'/%3e%3c/svg%3e");
    --mdb-accordion-btn-icon-width: 1.25rem;
    --mdb-accordion-btn-icon-transform: rotate(-180deg);
    --mdb-accordion-btn-icon-transition: transform 0.2s ease-in-out;
    --mdb-accordion-btn-active-icon: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%233b71ca'%3e%3cpath fill-rule='evenodd' d='M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z'/%3e%3c/svg%3e");
    --mdb-accordion-btn-focus-border-color: #3b71ca;
    --mdb-accordion-btn-focus-box-shadow: inset 0 -1px 0 var(--mdb-border-color);
    --mdb-accordion-body-padding-x: 1.5rem;
    --mdb-accordion-body-padding-y: 1.15rem;
    --mdb-accordion-active-color: #3b71ca;
    --mdb-accordion-active-bg: var(--mdb-surface-bg)
}

.accordion-button {
    position: relative;
    display: flex;
    align-items: center;
    width: 100%;
    padding: var(--mdb-accordion-btn-padding-y) var(--mdb-accordion-btn-padding-x);
    font-size: 1rem;
    color: var(--mdb-accordion-btn-color);
    text-align: left;
    background-color: var(--mdb-accordion-btn-bg);
    border: 0;
    border-radius: 0;
    overflow-anchor: none;
    transition: var(--mdb-accordion-transition)
}

@media(prefers-reduced-motion: reduce) {
    .accordion-button {
        transition: none
    }
}

.accordion-button:not(.collapsed) {
    color: var(--mdb-accordion-active-color);
    background-color: var(--mdb-accordion-active-bg);
    box-shadow: inset 0 calc(-1*var(--mdb-accordion-border-width)) 0 var(--mdb-accordion-border-color)
}

.accordion-button:not(.collapsed)::after {
    background-image: var(--mdb-accordion-btn-active-icon);
    transform: var(--mdb-accordion-btn-icon-transform)
}

.accordion-button::after {
    flex-shrink: 0;
    width: var(--mdb-accordion-btn-icon-width);
    height: var(--mdb-accordion-btn-icon-width);
    margin-left: auto;
    content: "";
    background-image: var(--mdb-accordion-btn-icon);
    background-repeat: no-repeat;
    background-size: var(--mdb-accordion-btn-icon-width);
    transition: var(--mdb-accordion-btn-icon-transition)
}

@media(prefers-reduced-motion: reduce) {
    .accordion-button::after {
        transition: none
    }
}

.accordion-button:hover {
    z-index: 2
}

.accordion-button:focus {
    z-index: 3;
    border-color: var(--mdb-accordion-btn-focus-border-color);
    outline: 0;
    box-shadow: var(--mdb-accordion-btn-focus-box-shadow)
}

.accordion-header {
    margin-bottom: 0
}

.accordion-item {
    color: var(--mdb-accordion-color);
    background-color: var(--mdb-accordion-bg);
    border: var(--mdb-accordion-border-width) solid var(--mdb-accordion-border-color)
}

.accordion-item:first-of-type {
    border-top-left-radius: var(--mdb-accordion-border-radius);
    border-top-right-radius: var(--mdb-accordion-border-radius)
}

.accordion-item:first-of-type .accordion-button {
    border-top-left-radius: var(--mdb-accordion-inner-border-radius);
    border-top-right-radius: var(--mdb-accordion-inner-border-radius)
}

.accordion-item:not(:first-of-type) {
    border-top: 0
}

.accordion-item:last-of-type {
    border-bottom-right-radius: var(--mdb-accordion-border-radius);
    border-bottom-left-radius: var(--mdb-accordion-border-radius)
}

.accordion-item:last-of-type .accordion-button.collapsed {
    border-bottom-right-radius: var(--mdb-accordion-inner-border-radius);
    border-bottom-left-radius: var(--mdb-accordion-inner-border-radius)
}

.accordion-item:last-of-type .accordion-collapse {
    border-bottom-right-radius: var(--mdb-accordion-border-radius);
    border-bottom-left-radius: var(--mdb-accordion-border-radius)
}

.accordion-body {
    padding: var(--mdb-accordion-body-padding-y) var(--mdb-accordion-body-padding-x)
}

.accordion-flush .accordion-collapse {
    border-width: 0
}

.accordion-flush .accordion-item {
    border-right: 0;
    border-left: 0;
    border-radius: 0
}

.accordion-flush .accordion-item:first-child {
    border-top: 0
}

.accordion-flush .accordion-item:last-child {
    border-bottom: 0
}

.accordion-flush .accordion-item .accordion-button,
.accordion-flush .accordion-item .accordion-button.collapsed {
    border-radius: 0
}

[data-mdb-theme=dark] .accordion-button::after {
    --mdb-accordion-btn-icon: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23fff'%3e%3cpath fill-rule='evenodd' d='M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z'/%3e%3c/svg%3e");
    --mdb-accordion-btn-active-icon: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%233b71ca'%3e%3cpath fill-rule='evenodd' d='M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z'/%3e%3c/svg%3e")
}

@keyframes progress-bar-stripes {
    0% {
        background-position-x: 4px
    }
}

.progress,
.progress-stacked {
    --mdb-progress-height: 4px;
    --mdb-progress-font-size: 0.75rem;
    --mdb-progress-bg: var(--mdb-secondary-bg);
    --mdb-progress-border-radius: var(--mdb-border-radius);
    --mdb-progress-box-shadow: var(--mdb-box-shadow-inset);
    --mdb-progress-bar-color: #fff;
    --mdb-progress-bar-bg: #3b71ca;
    --mdb-progress-bar-transition: width 0.6s ease;
    display: flex;
    height: var(--mdb-progress-height);
    overflow: hidden;
    font-size: var(--mdb-progress-font-size);
    background-color: var(--mdb-progress-bg);
    border-radius: var(--mdb-progress-border-radius);
    box-shadow: var(--mdb-progress-box-shadow)
}

.progress-bar {
    display: flex;
    flex-direction: column;
    justify-content: center;
    overflow: hidden;
    color: var(--mdb-progress-bar-color);
    text-align: center;
    white-space: nowrap;
    background-color: var(--mdb-progress-bar-bg);
    transition: var(--mdb-progress-bar-transition)
}

@media(prefers-reduced-motion: reduce) {
    .progress-bar {
        transition: none
    }
}

.progress-bar-striped {
    background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
    background-size: var(--mdb-progress-height) var(--mdb-progress-height)
}

.progress-stacked>.progress {
    overflow: visible
}

.progress-stacked>.progress>.progress-bar {
    width: 100%
}

.progress-bar-animated {
    animation: 1s linear infinite progress-bar-stripes
}

@media(prefers-reduced-motion: reduce) {
    .progress-bar-animated {
        animation: none
    }
}

.placeholder {
    display: inline-block;
    min-height: 1em;
    vertical-align: middle;
    cursor: wait;
    background-color: currentcolor;
    opacity: .5
}

.placeholder.btn::before {
    display: inline-block;
    content: ""
}

.placeholder-xs {
    min-height: .6em
}

.placeholder-sm {
    min-height: .8em
}

.placeholder-lg {
    min-height: 1.2em
}

.placeholder-glow .placeholder {
    animation: placeholder-glow 2s ease-in-out infinite
}

@keyframes placeholder-glow {
    50% {
        opacity: .2
    }
}

.placeholder-wave {
    mask-image: linear-gradient(130deg, #000 55%, rgba(0, 0, 0, 0.8) 75%, #000 95%);
    mask-size: 200% 100%;
    animation: placeholder-wave 2s linear infinite
}

@keyframes placeholder-wave {
    100% {
        mask-position: -200% 0%
    }
}

.list-group {
    --mdb-list-group-color: var(--mdb-body-color);
    --mdb-list-group-bg: transparent;
    --mdb-list-group-border-color: var(--mdb-border-color);
    --mdb-list-group-border-width: var(--mdb-border-width);
    --mdb-list-group-border-radius: 0.5rem;
    --mdb-list-group-item-padding-x: 1.5rem;
    --mdb-list-group-item-padding-y: 0.5rem;
    --mdb-list-group-action-color: var(--mdb-secondary-color);
    --mdb-list-group-action-hover-color: var(--mdb-emphasis-color);
    --mdb-list-group-action-hover-bg: var(--mdb-tertiary-bg);
    --mdb-list-group-action-active-color: var(--mdb-body-color);
    --mdb-list-group-action-active-bg: var(--mdb-secondary-bg);
    --mdb-list-group-disabled-color: rgba(var(--mdb-body-color-rgb), 0.5);
    --mdb-list-group-disabled-bg: transparent;
    --mdb-list-group-active-color: #fff;
    --mdb-list-group-active-bg: #3b71ca;
    --mdb-list-group-active-border-color: #3b71ca;
    display: flex;
    flex-direction: column;
    padding-left: 0;
    margin-bottom: 0;
    border-radius: var(--mdb-list-group-border-radius)
}

.list-group-numbered {
    list-style-type: none;
    counter-reset: section
}

.list-group-numbered>.list-group-item::before {
    content: counters(section, ".") ". ";
    counter-increment: section
}

.list-group-item-action {
    width: 100%;
    color: var(--mdb-list-group-action-color);
    text-align: inherit
}

.list-group-item-action:hover,
.list-group-item-action:focus {
    z-index: 1;
    color: var(--mdb-list-group-action-hover-color);
    text-decoration: none;
    background-color: var(--mdb-list-group-action-hover-bg)
}

.list-group-item-action:active {
    color: var(--mdb-list-group-action-active-color);
    background-color: var(--mdb-list-group-action-active-bg)
}

.list-group-item {
    position: relative;
    display: block;
    padding: var(--mdb-list-group-item-padding-y) var(--mdb-list-group-item-padding-x);
    color: var(--mdb-list-group-color);
    background-color: var(--mdb-list-group-bg);
    border: var(--mdb-list-group-border-width) solid var(--mdb-list-group-border-color)
}

.list-group-item:first-child {
    border-top-left-radius: inherit;
    border-top-right-radius: inherit
}

.list-group-item:last-child {
    border-bottom-right-radius: inherit;
    border-bottom-left-radius: inherit
}

.list-group-item.disabled,
.list-group-item:disabled {
    color: var(--mdb-list-group-disabled-color);
    pointer-events: none;
    background-color: var(--mdb-list-group-disabled-bg)
}

.list-group-item.active {
    z-index: 2;
    color: var(--mdb-list-group-active-color);
    background-color: var(--mdb-list-group-active-bg);
    border-color: var(--mdb-list-group-active-border-color)
}

.list-group-item+.list-group-item {
    border-top-width: 0
}

.list-group-item+.list-group-item.active {
    margin-top: calc(-1*var(--mdb-list-group-border-width));
    border-top-width: var(--mdb-list-group-border-width)
}

.list-group-horizontal {
    flex-direction: row
}

.list-group-horizontal>.list-group-item:first-child:not(:last-child) {
    border-bottom-left-radius: var(--mdb-list-group-border-radius);
    border-top-right-radius: 0
}

.list-group-horizontal>.list-group-item:last-child:not(:first-child) {
    border-top-right-radius: var(--mdb-list-group-border-radius);
    border-bottom-left-radius: 0
}

.list-group-horizontal>.list-group-item.active {
    margin-top: 0
}

.list-group-horizontal>.list-group-item+.list-group-item {
    border-top-width: var(--mdb-list-group-border-width);
    border-left-width: 0
}

.list-group-horizontal>.list-group-item+.list-group-item.active {
    margin-left: calc(-1*var(--mdb-list-group-border-width));
    border-left-width: var(--mdb-list-group-border-width)
}

@media(min-width: 576px) {
    .list-group-horizontal-sm {
        flex-direction: row
    }

    .list-group-horizontal-sm>.list-group-item:first-child:not(:last-child) {
        border-bottom-left-radius: var(--mdb-list-group-border-radius);
        border-top-right-radius: 0
    }

    .list-group-horizontal-sm>.list-group-item:last-child:not(:first-child) {
        border-top-right-radius: var(--mdb-list-group-border-radius);
        border-bottom-left-radius: 0
    }

    .list-group-horizontal-sm>.list-group-item.active {
        margin-top: 0
    }

    .list-group-horizontal-sm>.list-group-item+.list-group-item {
        border-top-width: var(--mdb-list-group-border-width);
        border-left-width: 0
    }

    .list-group-horizontal-sm>.list-group-item+.list-group-item.active {
        margin-left: calc(-1*var(--mdb-list-group-border-width));
        border-left-width: var(--mdb-list-group-border-width)
    }
}

@media(min-width: 768px) {
    .list-group-horizontal-md {
        flex-direction: row
    }

    .list-group-horizontal-md>.list-group-item:first-child:not(:last-child) {
        border-bottom-left-radius: var(--mdb-list-group-border-radius);
        border-top-right-radius: 0
    }

    .list-group-horizontal-md>.list-group-item:last-child:not(:first-child) {
        border-top-right-radius: var(--mdb-list-group-border-radius);
        border-bottom-left-radius: 0
    }

    .list-group-horizontal-md>.list-group-item.active {
        margin-top: 0
    }

    .list-group-horizontal-md>.list-group-item+.list-group-item {
        border-top-width: var(--mdb-list-group-border-width);
        border-left-width: 0
    }

    .list-group-horizontal-md>.list-group-item+.list-group-item.active {
        margin-left: calc(-1*var(--mdb-list-group-border-width));
        border-left-width: var(--mdb-list-group-border-width)
    }
}

@media(min-width: 992px) {
    .list-group-horizontal-lg {
        flex-direction: row
    }

    .list-group-horizontal-lg>.list-group-item:first-child:not(:last-child) {
        border-bottom-left-radius: var(--mdb-list-group-border-radius);
        border-top-right-radius: 0
    }

    .list-group-horizontal-lg>.list-group-item:last-child:not(:first-child) {
        border-top-right-radius: var(--mdb-list-group-border-radius);
        border-bottom-left-radius: 0
    }

    .list-group-horizontal-lg>.list-group-item.active {
        margin-top: 0
    }

    .list-group-horizontal-lg>.list-group-item+.list-group-item {
        border-top-width: var(--mdb-list-group-border-width);
        border-left-width: 0
    }

    .list-group-horizontal-lg>.list-group-item+.list-group-item.active {
        margin-left: calc(-1*var(--mdb-list-group-border-width));
        border-left-width: var(--mdb-list-group-border-width)
    }
}

@media(min-width: 1200px) {
    .list-group-horizontal-xl {
        flex-direction: row
    }

    .list-group-horizontal-xl>.list-group-item:first-child:not(:last-child) {
        border-bottom-left-radius: var(--mdb-list-group-border-radius);
        border-top-right-radius: 0
    }

    .list-group-horizontal-xl>.list-group-item:last-child:not(:first-child) {
        border-top-right-radius: var(--mdb-list-group-border-radius);
        border-bottom-left-radius: 0
    }

    .list-group-horizontal-xl>.list-group-item.active {
        margin-top: 0
    }

    .list-group-horizontal-xl>.list-group-item+.list-group-item {
        border-top-width: var(--mdb-list-group-border-width);
        border-left-width: 0
    }

    .list-group-horizontal-xl>.list-group-item+.list-group-item.active {
        margin-left: calc(-1*var(--mdb-list-group-border-width));
        border-left-width: var(--mdb-list-group-border-width)
    }
}

@media(min-width: 1400px) {
    .list-group-horizontal-xxl {
        flex-direction: row
    }

    .list-group-horizontal-xxl>.list-group-item:first-child:not(:last-child) {
        border-bottom-left-radius: var(--mdb-list-group-border-radius);
        border-top-right-radius: 0
    }

    .list-group-horizontal-xxl>.list-group-item:last-child:not(:first-child) {
        border-top-right-radius: var(--mdb-list-group-border-radius);
        border-bottom-left-radius: 0
    }

    .list-group-horizontal-xxl>.list-group-item.active {
        margin-top: 0
    }

    .list-group-horizontal-xxl>.list-group-item+.list-group-item {
        border-top-width: var(--mdb-list-group-border-width);
        border-left-width: 0
    }

    .list-group-horizontal-xxl>.list-group-item+.list-group-item.active {
        margin-left: calc(-1*var(--mdb-list-group-border-width));
        border-left-width: var(--mdb-list-group-border-width)
    }
}

.list-group-flush {
    border-radius: 0
}

.list-group-flush>.list-group-item {
    border-width: 0 0 var(--mdb-list-group-border-width)
}

.list-group-flush>.list-group-item:last-child {
    border-bottom-width: 0
}

.list-group-item-primary {
    --mdb-list-group-color: var(--mdb-primary-text-emphasis);
    --mdb-list-group-bg: var(--mdb-primary-bg-subtle);
    --mdb-list-group-border-color: var(--mdb-primary-border-subtle);
    --mdb-list-group-action-hover-color: var(--mdb-emphasis-color);
    --mdb-list-group-action-hover-bg: var(--mdb-primary-border-subtle);
    --mdb-list-group-action-active-color: var(--mdb-emphasis-color);
    --mdb-list-group-action-active-bg: var(--mdb-primary-border-subtle);
    --mdb-list-group-active-color: var(--mdb-primary-bg-subtle);
    --mdb-list-group-active-bg: var(--mdb-primary-text-emphasis);
    --mdb-list-group-active-border-color: var(--mdb-primary-text-emphasis)
}

.list-group-item-secondary {
    --mdb-list-group-color: var(--mdb-secondary-text-emphasis);
    --mdb-list-group-bg: var(--mdb-secondary-bg-subtle);
    --mdb-list-group-border-color: var(--mdb-secondary-border-subtle);
    --mdb-list-group-action-hover-color: var(--mdb-emphasis-color);
    --mdb-list-group-action-hover-bg: var(--mdb-secondary-border-subtle);
    --mdb-list-group-action-active-color: var(--mdb-emphasis-color);
    --mdb-list-group-action-active-bg: var(--mdb-secondary-border-subtle);
    --mdb-list-group-active-color: var(--mdb-secondary-bg-subtle);
    --mdb-list-group-active-bg: var(--mdb-secondary-text-emphasis);
    --mdb-list-group-active-border-color: var(--mdb-secondary-text-emphasis)
}

.list-group-item-success {
    --mdb-list-group-color: var(--mdb-success-text-emphasis);
    --mdb-list-group-bg: var(--mdb-success-bg-subtle);
    --mdb-list-group-border-color: var(--mdb-success-border-subtle);
    --mdb-list-group-action-hover-color: var(--mdb-emphasis-color);
    --mdb-list-group-action-hover-bg: var(--mdb-success-border-subtle);
    --mdb-list-group-action-active-color: var(--mdb-emphasis-color);
    --mdb-list-group-action-active-bg: var(--mdb-success-border-subtle);
    --mdb-list-group-active-color: var(--mdb-success-bg-subtle);
    --mdb-list-group-active-bg: var(--mdb-success-text-emphasis);
    --mdb-list-group-active-border-color: var(--mdb-success-text-emphasis)
}

.list-group-item-danger {
    --mdb-list-group-color: var(--mdb-danger-text-emphasis);
    --mdb-list-group-bg: var(--mdb-danger-bg-subtle);
    --mdb-list-group-border-color: var(--mdb-danger-border-subtle);
    --mdb-list-group-action-hover-color: var(--mdb-emphasis-color);
    --mdb-list-group-action-hover-bg: var(--mdb-danger-border-subtle);
    --mdb-list-group-action-active-color: var(--mdb-emphasis-color);
    --mdb-list-group-action-active-bg: var(--mdb-danger-border-subtle);
    --mdb-list-group-active-color: var(--mdb-danger-bg-subtle);
    --mdb-list-group-active-bg: var(--mdb-danger-text-emphasis);
    --mdb-list-group-active-border-color: var(--mdb-danger-text-emphasis)
}

.list-group-item-warning {
    --mdb-list-group-color: var(--mdb-warning-text-emphasis);
    --mdb-list-group-bg: var(--mdb-warning-bg-subtle);
    --mdb-list-group-border-color: var(--mdb-warning-border-subtle);
    --mdb-list-group-action-hover-color: var(--mdb-emphasis-color);
    --mdb-list-group-action-hover-bg: var(--mdb-warning-border-subtle);
    --mdb-list-group-action-active-color: var(--mdb-emphasis-color);
    --mdb-list-group-action-active-bg: var(--mdb-warning-border-subtle);
    --mdb-list-group-active-color: var(--mdb-warning-bg-subtle);
    --mdb-list-group-active-bg: var(--mdb-warning-text-emphasis);
    --mdb-list-group-active-border-color: var(--mdb-warning-text-emphasis)
}

.list-group-item-info {
    --mdb-list-group-color: var(--mdb-info-text-emphasis);
    --mdb-list-group-bg: var(--mdb-info-bg-subtle);
    --mdb-list-group-border-color: var(--mdb-info-border-subtle);
    --mdb-list-group-action-hover-color: var(--mdb-emphasis-color);
    --mdb-list-group-action-hover-bg: var(--mdb-info-border-subtle);
    --mdb-list-group-action-active-color: var(--mdb-emphasis-color);
    --mdb-list-group-action-active-bg: var(--mdb-info-border-subtle);
    --mdb-list-group-active-color: var(--mdb-info-bg-subtle);
    --mdb-list-group-active-bg: var(--mdb-info-text-emphasis);
    --mdb-list-group-active-border-color: var(--mdb-info-text-emphasis)
}

.list-group-item-light {
    --mdb-list-group-color: var(--mdb-light-text-emphasis);
    --mdb-list-group-bg: var(--mdb-light-bg-subtle);
    --mdb-list-group-border-color: var(--mdb-light-border-subtle);
    --mdb-list-group-action-hover-color: var(--mdb-emphasis-color);
    --mdb-list-group-action-hover-bg: var(--mdb-light-border-subtle);
    --mdb-list-group-action-active-color: var(--mdb-emphasis-color);
    --mdb-list-group-action-active-bg: var(--mdb-light-border-subtle);
    --mdb-list-group-active-color: var(--mdb-light-bg-subtle);
    --mdb-list-group-active-bg: var(--mdb-light-text-emphasis);
    --mdb-list-group-active-border-color: var(--mdb-light-text-emphasis)
}

.list-group-item-dark {
    --mdb-list-group-color: var(--mdb-dark-text-emphasis);
    --mdb-list-group-bg: var(--mdb-dark-bg-subtle);
    --mdb-list-group-border-color: var(--mdb-dark-border-subtle);
    --mdb-list-group-action-hover-color: var(--mdb-emphasis-color);
    --mdb-list-group-action-hover-bg: var(--mdb-dark-border-subtle);
    --mdb-list-group-action-active-color: var(--mdb-emphasis-color);
    --mdb-list-group-action-active-bg: var(--mdb-dark-border-subtle);
    --mdb-list-group-active-color: var(--mdb-dark-bg-subtle);
    --mdb-list-group-active-bg: var(--mdb-dark-text-emphasis);
    --mdb-list-group-active-border-color: var(--mdb-dark-text-emphasis)
}

.btn-close {
    --mdb-btn-close-color: #000;
    --mdb-btn-close-bg: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23000'%3e%3cpath d='M.293.293a1 1 0 0 1 1.414 0L8 6.586 14.293.293a1 1 0 1 1 1.414 1.414L9.414 8l6.293 6.293a1 1 0 0 1-1.414 1.414L8 9.414l-6.293 6.293a1 1 0 0 1-1.414-1.414L6.586 8 .293 1.707a1 1 0 0 1 0-1.414z'/%3e%3c/svg%3e");
    --mdb-btn-close-opacity: 0.5;
    --mdb-btn-close-hover-opacity: 0.75;
    --mdb-btn-close-focus-shadow: 0 0 0 0.25rem rgba(59, 113, 202, 0.25);
    --mdb-btn-close-focus-opacity: 1;
    --mdb-btn-close-disabled-opacity: 0.25;
    --mdb-btn-close-white-filter: invert(1) grayscale(100%) brightness(200%);
    box-sizing: content-box;
    width: 1em;
    height: 1em;
    padding: .25em .25em;
    color: var(--mdb-btn-close-color);
    background: rgba(0, 0, 0, 0) var(--mdb-btn-close-bg) center/1em auto no-repeat;
    border: 0;
    border-radius: .25rem;
    opacity: var(--mdb-btn-close-opacity)
}

.btn-close:hover {
    color: var(--mdb-btn-close-color);
    text-decoration: none;
    opacity: var(--mdb-btn-close-hover-opacity)
}

.btn-close:focus {
    outline: 0;
    box-shadow: var(--mdb-btn-close-focus-shadow);
    opacity: var(--mdb-btn-close-focus-opacity)
}

.btn-close:disabled,
.btn-close.disabled {
    pointer-events: none;
    user-select: none;
    opacity: var(--mdb-btn-close-disabled-opacity)
}

.btn-close-white {
    filter: var(--mdb-btn-close-white-filter)
}

[data-mdb-theme=dark] .btn-close {
    filter: var(--mdb-btn-close-white-filter)
}

.toast {
    --mdb-toast-zindex: 1060;
    --mdb-toast-padding-x: 1rem;
    --mdb-toast-padding-y: 0.65rem;
    --mdb-toast-spacing: 1.5rem;
    --mdb-toast-max-width: 350px;
    --mdb-toast-font-size: 0.875rem;
    --mdb-toast-color: ;
    --mdb-toast-bg: var(--mdb-surface-bg);
    --mdb-toast-border-width: var(--mdb-border-width);
    --mdb-toast-border-color: var(--mdb-border-color-translucent);
    --mdb-toast-border-radius: 0.5rem;
    --mdb-toast-box-shadow: 0 2px 15px -3px rgba(var(--mdb-box-shadow-color-rgb), 0.07), 0 10px 20px -2px rgba(var(--mdb-box-shadow-color-rgb), 0.04);
    --mdb-toast-header-color: var(--mdb-secondary-color);
    --mdb-toast-header-bg: var(--mdb-surface-bg);
    --mdb-toast-header-border-color: var(--mdb-border-color-translucent);
    width: var(--mdb-toast-max-width);
    max-width: 100%;
    font-size: var(--mdb-toast-font-size);
    color: var(--mdb-toast-color);
    pointer-events: auto;
    background-color: var(--mdb-toast-bg);
    background-clip: padding-box;
    border: var(--mdb-toast-border-width) solid var(--mdb-toast-border-color);
    box-shadow: var(--mdb-toast-box-shadow);
    border-radius: var(--mdb-toast-border-radius)
}

.toast.showing {
    opacity: 0
}

.toast:not(.show) {
    display: none
}

.toast-container {
    --mdb-toast-zindex: 1060;
    position: absolute;
    z-index: var(--mdb-toast-zindex);
    width: max-content;
    max-width: 100%;
    pointer-events: none
}

.toast-container>:not(:last-child) {
    margin-bottom: var(--mdb-toast-spacing)
}

.toast-header {
    display: flex;
    align-items: center;
    padding: var(--mdb-toast-padding-y) var(--mdb-toast-padding-x);
    color: var(--mdb-toast-header-color);
    background-color: var(--mdb-toast-header-bg);
    background-clip: padding-box;
    border-bottom: var(--mdb-toast-border-width) solid var(--mdb-toast-header-border-color);
    border-top-left-radius: calc(var(--mdb-toast-border-radius) - var(--mdb-toast-border-width));
    border-top-right-radius: calc(var(--mdb-toast-border-radius) - var(--mdb-toast-border-width))
}

.toast-header .btn-close {
    margin-right: calc(-0.5*var(--mdb-toast-padding-x));
    margin-left: var(--mdb-toast-padding-x)
}

.toast-body {
    padding: var(--mdb-toast-padding-x);
    word-wrap: break-word
}

.modal {
    --mdb-modal-zindex: 1055;
    --mdb-modal-width: 500px;
    --mdb-modal-padding: 1rem;
    --mdb-modal-margin: 0.5rem;
    --mdb-modal-color: var(--mdb-surface-color);
    --mdb-modal-bg: var(--mdb-surface-bg);
    --mdb-modal-border-color: var(--mdb-border-color-translucent);
    --mdb-modal-border-width: var(--mdb-border-width);
    --mdb-modal-border-radius: 0.5rem;
    --mdb-modal-box-shadow: var(--mdb-box-shadow-sm);
    --mdb-modal-inner-border-radius: calc(0.5rem - (var(--mdb-border-width)));
    --mdb-modal-header-padding-x: 1rem;
    --mdb-modal-header-padding-y: 1rem;
    --mdb-modal-header-padding: 1rem 1rem;
    --mdb-modal-header-border-color: var(--mdb-divider-color);
    --mdb-modal-header-border-width: 2px;
    --mdb-modal-title-line-height: 1.6;
    --mdb-modal-footer-gap: 0.5rem;
    --mdb-modal-footer-bg: ;
    --mdb-modal-footer-border-color: var(--mdb-divider-color);
    --mdb-modal-footer-border-width: 2px;
    position: fixed;
    top: 0;
    left: 0;
    z-index: var(--mdb-modal-zindex);
    display: none;
    width: 100%;
    height: 100%;
    overflow-x: hidden;
    overflow-y: auto;
    outline: 0
}

.modal-dialog {
    position: relative;
    width: auto;
    margin: var(--mdb-modal-margin);
    pointer-events: none
}

.modal.fade .modal-dialog {
    transition: transform .3s ease-out;
    transform: translate(0, -50px)
}

@media(prefers-reduced-motion: reduce) {
    .modal.fade .modal-dialog {
        transition: none
    }
}

.modal.show .modal-dialog {
    transform: none
}

.modal.modal-static .modal-dialog {
    transform: scale(1.02)
}

.modal-dialog-scrollable {
    height: calc(100% - var(--mdb-modal-margin)*2)
}

.modal-dialog-scrollable .modal-content {
    max-height: 100%;
    overflow: hidden
}

.modal-dialog-scrollable .modal-body {
    overflow-y: auto
}

.modal-dialog-centered {
    display: flex;
    align-items: center;
    min-height: calc(100% - var(--mdb-modal-margin)*2)
}

.modal-content {
    position: relative;
    display: flex;
    flex-direction: column;
    width: 100%;
    color: var(--mdb-modal-color);
    pointer-events: auto;
    background-color: var(--mdb-modal-bg);
    background-clip: padding-box;
    border: var(--mdb-modal-border-width) solid var(--mdb-modal-border-color);
    border-radius: var(--mdb-modal-border-radius);
    box-shadow: var(--mdb-modal-box-shadow);
    outline: 0
}

.modal-backdrop {
    --mdb-backdrop-zindex: 1050;
    --mdb-backdrop-bg: #000;
    --mdb-backdrop-opacity: 0.5;
    position: fixed;
    top: 0;
    left: 0;
    z-index: var(--mdb-backdrop-zindex);
    width: 100vw;
    height: 100vh;
    background-color: var(--mdb-backdrop-bg)
}

.modal-backdrop.fade {
    opacity: 0
}

.modal-backdrop.show {
    opacity: var(--mdb-backdrop-opacity)
}

.modal-header {
    display: flex;
    flex-shrink: 0;
    align-items: center;
    justify-content: space-between;
    padding: var(--mdb-modal-header-padding);
    border-bottom: var(--mdb-modal-header-border-width) solid var(--mdb-modal-header-border-color);
    border-top-left-radius: var(--mdb-modal-inner-border-radius);
    border-top-right-radius: var(--mdb-modal-inner-border-radius)
}

.modal-header .btn-close {
    padding: calc(var(--mdb-modal-header-padding-y)*.5) calc(var(--mdb-modal-header-padding-x)*.5);
    margin: calc(-0.5*var(--mdb-modal-header-padding-y)) calc(-0.5*var(--mdb-modal-header-padding-x)) calc(-0.5*var(--mdb-modal-header-padding-y)) auto
}

.modal-title {
    margin-bottom: 0;
    line-height: var(--mdb-modal-title-line-height)
}

.modal-body {
    position: relative;
    flex: 1 1 auto;
    padding: var(--mdb-modal-padding)
}

.modal-footer {
    display: flex;
    flex-shrink: 0;
    flex-wrap: wrap;
    align-items: center;
    justify-content: flex-end;
    padding: calc(var(--mdb-modal-padding) - var(--mdb-modal-footer-gap)*.5);
    background-color: var(--mdb-modal-footer-bg);
    border-top: var(--mdb-modal-footer-border-width) solid var(--mdb-modal-footer-border-color);
    border-bottom-right-radius: var(--mdb-modal-inner-border-radius);
    border-bottom-left-radius: var(--mdb-modal-inner-border-radius)
}

.modal-footer>* {
    margin: calc(var(--mdb-modal-footer-gap)*.5)
}

@media(min-width: 576px) {
    .modal {
        --mdb-modal-margin: 1.75rem;
        --mdb-modal-box-shadow: var(--mdb-box-shadow)
    }

    .modal-dialog {
        max-width: var(--mdb-modal-width);
        margin-right: auto;
        margin-left: auto
    }

    .modal-sm {
        --mdb-modal-width: 300px
    }
}

@media(min-width: 992px) {

    .modal-lg,
    .modal-xl {
        --mdb-modal-width: 800px
    }
}

@media(min-width: 1200px) {
    .modal-xl {
        --mdb-modal-width: 1140px
    }
}

.modal-fullscreen {
    width: 100vw;
    max-width: none;
    height: 100%;
    margin: 0
}

.modal-fullscreen .modal-content {
    height: 100%;
    border: 0;
    border-radius: 0
}

.modal-fullscreen .modal-header,
.modal-fullscreen .modal-footer {
    border-radius: 0
}

.modal-fullscreen .modal-body {
    overflow-y: auto
}

@media(max-width: 575.98px) {
    .modal-fullscreen-sm-down {
        width: 100vw;
        max-width: none;
        height: 100%;
        margin: 0
    }

    .modal-fullscreen-sm-down .modal-content {
        height: 100%;
        border: 0;
        border-radius: 0
    }

    .modal-fullscreen-sm-down .modal-header,
    .modal-fullscreen-sm-down .modal-footer {
        border-radius: 0
    }

    .modal-fullscreen-sm-down .modal-body {
        overflow-y: auto
    }
}

@media(max-width: 767.98px) {
    .modal-fullscreen-md-down {
        width: 100vw;
        max-width: none;
        height: 100%;
        margin: 0
    }

    .modal-fullscreen-md-down .modal-content {
        height: 100%;
        border: 0;
        border-radius: 0
    }

    .modal-fullscreen-md-down .modal-header,
    .modal-fullscreen-md-down .modal-footer {
        border-radius: 0
    }

    .modal-fullscreen-md-down .modal-body {
        overflow-y: auto
    }
}

@media(max-width: 991.98px) {
    .modal-fullscreen-lg-down {
        width: 100vw;
        max-width: none;
        height: 100%;
        margin: 0
    }

    .modal-fullscreen-lg-down .modal-content {
        height: 100%;
        border: 0;
        border-radius: 0
    }

    .modal-fullscreen-lg-down .modal-header,
    .modal-fullscreen-lg-down .modal-footer {
        border-radius: 0
    }

    .modal-fullscreen-lg-down .modal-body {
        overflow-y: auto
    }
}

@media(max-width: 1199.98px) {
    .modal-fullscreen-xl-down {
        width: 100vw;
        max-width: none;
        height: 100%;
        margin: 0
    }

    .modal-fullscreen-xl-down .modal-content {
        height: 100%;
        border: 0;
        border-radius: 0
    }

    .modal-fullscreen-xl-down .modal-header,
    .modal-fullscreen-xl-down .modal-footer {
        border-radius: 0
    }

    .modal-fullscreen-xl-down .modal-body {
        overflow-y: auto
    }
}

@media(max-width: 1399.98px) {
    .modal-fullscreen-xxl-down {
        width: 100vw;
        max-width: none;
        height: 100%;
        margin: 0
    }

    .modal-fullscreen-xxl-down .modal-content {
        height: 100%;
        border: 0;
        border-radius: 0
    }

    .modal-fullscreen-xxl-down .modal-header,
    .modal-fullscreen-xxl-down .modal-footer {
        border-radius: 0
    }

    .modal-fullscreen-xxl-down .modal-body {
        overflow-y: auto
    }
}

.popover {
    --mdb-popover-zindex: 1080;
    --mdb-popover-max-width: 276px;
    --mdb-popover-font-size: 0.875rem;
    --mdb-popover-bg: var(--mdb-surface-bg);
    --mdb-popover-border-width: 1px;
    --mdb-popover-border-color: var(--mdb-divider-color);
    --mdb-popover-border-radius: 0.5rem;
    --mdb-popover-inner-border-radius: calc(0.5rem - 1px);
    --mdb-popover-box-shadow: 0 0px 3px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.07), 0 2px 2px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.04);
    --mdb-popover-header-padding-x: 1rem;
    --mdb-popover-header-padding-y: 0.5rem;
    --mdb-popover-header-font-size: 1rem;
    --mdb-popover-header-color: var(--mdb-surface-color);
    --mdb-popover-header-bg: var(--mdb-surface-bg);
    --mdb-popover-body-padding-x: 1rem;
    --mdb-popover-body-padding-y: 1rem;
    --mdb-popover-body-color: var(--mdb-surface-color);
    --mdb-popover-arrow-width: 1rem;
    --mdb-popover-arrow-height: 0.5rem;
    --mdb-popover-arrow-border: var(--mdb-popover-border-color);
    z-index: var(--mdb-popover-zindex);
    display: block;
    max-width: var(--mdb-popover-max-width);
    font-family: var(--mdb-font-roboto);
    font-style: normal;
    font-weight: 400;
    line-height: 1.6;
    text-align: left;
    text-align: start;
    text-decoration: none;
    text-shadow: none;
    text-transform: none;
    letter-spacing: normal;
    word-break: normal;
    white-space: normal;
    word-spacing: normal;
    line-break: auto;
    font-size: var(--mdb-popover-font-size);
    word-wrap: break-word;
    background-color: var(--mdb-popover-bg);
    background-clip: padding-box;
    border: var(--mdb-popover-border-width) solid var(--mdb-popover-border-color);
    border-radius: var(--mdb-popover-border-radius);
    box-shadow: var(--mdb-popover-box-shadow)
}

.popover .popover-arrow {
    display: block;
    width: var(--mdb-popover-arrow-width);
    height: var(--mdb-popover-arrow-height)
}

.popover .popover-arrow::before,
.popover .popover-arrow::after {
    position: absolute;
    display: block;
    content: "";
    border-color: rgba(0, 0, 0, 0);
    border-style: solid;
    border-width: 0
}

.bs-popover-top>.popover-arrow,
.bs-popover-auto[data-popper-placement^=top]>.popover-arrow {
    bottom: calc(-1*(var(--mdb-popover-arrow-height)) - var(--mdb-popover-border-width))
}

.bs-popover-top>.popover-arrow::before,
.bs-popover-auto[data-popper-placement^=top]>.popover-arrow::before,
.bs-popover-top>.popover-arrow::after,
.bs-popover-auto[data-popper-placement^=top]>.popover-arrow::after {
    border-width: var(--mdb-popover-arrow-height) calc(var(--mdb-popover-arrow-width)*.5) 0
}

.bs-popover-top>.popover-arrow::before,
.bs-popover-auto[data-popper-placement^=top]>.popover-arrow::before {
    bottom: 0;
    border-top-color: var(--mdb-popover-arrow-border)
}

.bs-popover-top>.popover-arrow::after,
.bs-popover-auto[data-popper-placement^=top]>.popover-arrow::after {
    bottom: var(--mdb-popover-border-width);
    border-top-color: var(--mdb-popover-bg)
}

.bs-popover-end>.popover-arrow,
.bs-popover-auto[data-popper-placement^=right]>.popover-arrow {
    left: calc(-1*(var(--mdb-popover-arrow-height)) - var(--mdb-popover-border-width));
    width: var(--mdb-popover-arrow-height);
    height: var(--mdb-popover-arrow-width)
}

.bs-popover-end>.popover-arrow::before,
.bs-popover-auto[data-popper-placement^=right]>.popover-arrow::before,
.bs-popover-end>.popover-arrow::after,
.bs-popover-auto[data-popper-placement^=right]>.popover-arrow::after {
    border-width: calc(var(--mdb-popover-arrow-width)*.5) var(--mdb-popover-arrow-height) calc(var(--mdb-popover-arrow-width)*.5) 0
}

.bs-popover-end>.popover-arrow::before,
.bs-popover-auto[data-popper-placement^=right]>.popover-arrow::before {
    left: 0;
    border-right-color: var(--mdb-popover-arrow-border)
}

.bs-popover-end>.popover-arrow::after,
.bs-popover-auto[data-popper-placement^=right]>.popover-arrow::after {
    left: var(--mdb-popover-border-width);
    border-right-color: var(--mdb-popover-bg)
}

.bs-popover-bottom>.popover-arrow,
.bs-popover-auto[data-popper-placement^=bottom]>.popover-arrow {
    top: calc(-1*(var(--mdb-popover-arrow-height)) - var(--mdb-popover-border-width))
}

.bs-popover-bottom>.popover-arrow::before,
.bs-popover-auto[data-popper-placement^=bottom]>.popover-arrow::before,
.bs-popover-bottom>.popover-arrow::after,
.bs-popover-auto[data-popper-placement^=bottom]>.popover-arrow::after {
    border-width: 0 calc(var(--mdb-popover-arrow-width)*.5) var(--mdb-popover-arrow-height)
}

.bs-popover-bottom>.popover-arrow::before,
.bs-popover-auto[data-popper-placement^=bottom]>.popover-arrow::before {
    top: 0;
    border-bottom-color: var(--mdb-popover-arrow-border)
}

.bs-popover-bottom>.popover-arrow::after,
.bs-popover-auto[data-popper-placement^=bottom]>.popover-arrow::after {
    top: var(--mdb-popover-border-width);
    border-bottom-color: var(--mdb-popover-bg)
}

.bs-popover-bottom .popover-header::before,
.bs-popover-auto[data-popper-placement^=bottom] .popover-header::before {
    position: absolute;
    top: 0;
    left: 50%;
    display: block;
    width: var(--mdb-popover-arrow-width);
    margin-left: calc(-0.5*var(--mdb-popover-arrow-width));
    content: "";
    border-bottom: var(--mdb-popover-border-width) solid var(--mdb-popover-header-bg)
}

.bs-popover-start>.popover-arrow,
.bs-popover-auto[data-popper-placement^=left]>.popover-arrow {
    right: calc(-1*(var(--mdb-popover-arrow-height)) - var(--mdb-popover-border-width));
    width: var(--mdb-popover-arrow-height);
    height: var(--mdb-popover-arrow-width)
}

.bs-popover-start>.popover-arrow::before,
.bs-popover-auto[data-popper-placement^=left]>.popover-arrow::before,
.bs-popover-start>.popover-arrow::after,
.bs-popover-auto[data-popper-placement^=left]>.popover-arrow::after {
    border-width: calc(var(--mdb-popover-arrow-width)*.5) 0 calc(var(--mdb-popover-arrow-width)*.5) var(--mdb-popover-arrow-height)
}

.bs-popover-start>.popover-arrow::before,
.bs-popover-auto[data-popper-placement^=left]>.popover-arrow::before {
    right: 0;
    border-left-color: var(--mdb-popover-arrow-border)
}

.bs-popover-start>.popover-arrow::after,
.bs-popover-auto[data-popper-placement^=left]>.popover-arrow::after {
    right: var(--mdb-popover-border-width);
    border-left-color: var(--mdb-popover-bg)
}

.popover-header {
    padding: var(--mdb-popover-header-padding-y) var(--mdb-popover-header-padding-x);
    margin-bottom: 0;
    font-size: var(--mdb-popover-header-font-size);
    color: var(--mdb-popover-header-color);
    background-color: var(--mdb-popover-header-bg);
    border-bottom: var(--mdb-popover-border-width) solid var(--mdb-popover-border-color);
    border-top-left-radius: var(--mdb-popover-inner-border-radius);
    border-top-right-radius: var(--mdb-popover-inner-border-radius)
}

.popover-header:empty {
    display: none
}

.popover-body {
    padding: var(--mdb-popover-body-padding-y) var(--mdb-popover-body-padding-x);
    color: var(--mdb-popover-body-color)
}

.spinner-grow,
.spinner-border {
    display: inline-block;
    width: var(--mdb-spinner-width);
    height: var(--mdb-spinner-height);
    vertical-align: var(--mdb-spinner-vertical-align);
    border-radius: 50%;
    animation: var(--mdb-spinner-animation-speed) linear infinite var(--mdb-spinner-animation-name)
}

@keyframes spinner-border {
    to {
        transform: rotate(360deg)
            /*!rtl:ignore*/
    }
}

.spinner-border {
    --mdb-spinner-width: 2rem;
    --mdb-spinner-height: 2rem;
    --mdb-spinner-vertical-align: -0.125em;
    --mdb-spinner-border-width: 0.25em;
    --mdb-spinner-animation-speed: 0.75s;
    --mdb-spinner-animation-name: spinner-border;
    border: var(--mdb-spinner-border-width) solid currentcolor;
    border-right-color: rgba(0, 0, 0, 0)
}

.spinner-border-sm {
    --mdb-spinner-width: 1rem;
    --mdb-spinner-height: 1rem;
    --mdb-spinner-border-width: 0.2em
}

@keyframes spinner-grow {
    0% {
        transform: scale(0)
    }

    50% {
        opacity: 1;
        transform: none
    }
}

.spinner-grow {
    --mdb-spinner-width: 2rem;
    --mdb-spinner-height: 2rem;
    --mdb-spinner-vertical-align: -0.125em;
    --mdb-spinner-animation-speed: 0.75s;
    --mdb-spinner-animation-name: spinner-grow;
    background-color: currentcolor;
    opacity: 0
}

.spinner-grow-sm {
    --mdb-spinner-width: 1rem;
    --mdb-spinner-height: 1rem
}

@media(prefers-reduced-motion: reduce) {

    .spinner-border,
    .spinner-grow {
        --mdb-spinner-animation-speed: 1.5s
    }
}

.tooltip {
    --mdb-tooltip-zindex: 1090;
    --mdb-tooltip-max-width: 200px;
    --mdb-tooltip-padding-x: 16px;
    --mdb-tooltip-padding-y: 6px;
    --mdb-tooltip-margin: ;
    --mdb-tooltip-font-size: 0.875rem;
    --mdb-tooltip-color: var(--mdb-surface-inverted-color);
    --mdb-tooltip-bg: var(--mdb-surface-inverted-bg);
    --mdb-tooltip-border-radius: 0.25rem;
    --mdb-tooltip-opacity: 0.9;
    --mdb-tooltip-arrow-width: 0.8rem;
    --mdb-tooltip-arrow-height: 0.4rem;
    z-index: var(--mdb-tooltip-zindex);
    display: block;
    margin: var(--mdb-tooltip-margin);
    font-family: var(--mdb-font-roboto);
    font-style: normal;
    font-weight: 400;
    line-height: 1.6;
    text-align: left;
    text-align: start;
    text-decoration: none;
    text-shadow: none;
    text-transform: none;
    letter-spacing: normal;
    word-break: normal;
    white-space: normal;
    word-spacing: normal;
    line-break: auto;
    font-size: var(--mdb-tooltip-font-size);
    word-wrap: break-word;
    opacity: 0
}

.tooltip.show {
    opacity: var(--mdb-tooltip-opacity)
}

.tooltip .tooltip-arrow {
    display: block;
    width: var(--mdb-tooltip-arrow-width);
    height: var(--mdb-tooltip-arrow-height)
}

.tooltip .tooltip-arrow::before {
    position: absolute;
    content: "";
    border-color: rgba(0, 0, 0, 0);
    border-style: solid
}

.bs-tooltip-top .tooltip-arrow,
.bs-tooltip-auto[data-popper-placement^=top] .tooltip-arrow {
    bottom: calc(-1*var(--mdb-tooltip-arrow-height))
}

.bs-tooltip-top .tooltip-arrow::before,
.bs-tooltip-auto[data-popper-placement^=top] .tooltip-arrow::before {
    top: -1px;
    border-width: var(--mdb-tooltip-arrow-height) calc(var(--mdb-tooltip-arrow-width)*.5) 0;
    border-top-color: var(--mdb-tooltip-bg)
}

.bs-tooltip-end .tooltip-arrow,
.bs-tooltip-auto[data-popper-placement^=right] .tooltip-arrow {
    left: calc(-1*var(--mdb-tooltip-arrow-height));
    width: var(--mdb-tooltip-arrow-height);
    height: var(--mdb-tooltip-arrow-width)
}

.bs-tooltip-end .tooltip-arrow::before,
.bs-tooltip-auto[data-popper-placement^=right] .tooltip-arrow::before {
    right: -1px;
    border-width: calc(var(--mdb-tooltip-arrow-width)*.5) var(--mdb-tooltip-arrow-height) calc(var(--mdb-tooltip-arrow-width)*.5) 0;
    border-right-color: var(--mdb-tooltip-bg)
}

.bs-tooltip-bottom .tooltip-arrow,
.bs-tooltip-auto[data-popper-placement^=bottom] .tooltip-arrow {
    top: calc(-1*var(--mdb-tooltip-arrow-height))
}

.bs-tooltip-bottom .tooltip-arrow::before,
.bs-tooltip-auto[data-popper-placement^=bottom] .tooltip-arrow::before {
    bottom: -1px;
    border-width: 0 calc(var(--mdb-tooltip-arrow-width)*.5) var(--mdb-tooltip-arrow-height);
    border-bottom-color: var(--mdb-tooltip-bg)
}

.bs-tooltip-start .tooltip-arrow,
.bs-tooltip-auto[data-popper-placement^=left] .tooltip-arrow {
    right: calc(-1*var(--mdb-tooltip-arrow-height));
    width: var(--mdb-tooltip-arrow-height);
    height: var(--mdb-tooltip-arrow-width)
}

.bs-tooltip-start .tooltip-arrow::before,
.bs-tooltip-auto[data-popper-placement^=left] .tooltip-arrow::before {
    left: -1px;
    border-width: calc(var(--mdb-tooltip-arrow-width)*.5) 0 calc(var(--mdb-tooltip-arrow-width)*.5) var(--mdb-tooltip-arrow-height);
    border-left-color: var(--mdb-tooltip-bg)
}

.tooltip-inner {
    max-width: var(--mdb-tooltip-max-width);
    padding: var(--mdb-tooltip-padding-y) var(--mdb-tooltip-padding-x);
    color: var(--mdb-tooltip-color);
    text-align: center;
    background-color: var(--mdb-tooltip-bg);
    border-radius: var(--mdb-tooltip-border-radius)
}

.clearfix::after {
    display: block;
    clear: both;
    content: ""
}

.text-bg-primary {
    color: #fff !important;
    background-color: RGBA(var(--mdb-primary-rgb), var(--mdb-bg-opacity, 1)) !important
}

.text-bg-secondary {
    color: #fff !important;
    background-color: RGBA(var(--mdb-secondary-rgb), var(--mdb-bg-opacity, 1)) !important
}

.text-bg-success {
    color: #fff !important;
    background-color: RGBA(var(--mdb-success-rgb), var(--mdb-bg-opacity, 1)) !important
}

.text-bg-danger {
    color: #fff !important;
    background-color: RGBA(var(--mdb-danger-rgb), var(--mdb-bg-opacity, 1)) !important
}

.text-bg-warning {
    color: #fff !important;
    background-color: RGBA(var(--mdb-warning-rgb), var(--mdb-bg-opacity, 1)) !important
}

.text-bg-info {
    color: #fff !important;
    background-color: RGBA(var(--mdb-info-rgb), var(--mdb-bg-opacity, 1)) !important
}

.text-bg-light {
    color: #000 !important;
    background-color: RGBA(var(--mdb-light-rgb), var(--mdb-bg-opacity, 1)) !important
}

.text-bg-dark {
    color: #fff !important;
    background-color: RGBA(var(--mdb-dark-rgb), var(--mdb-bg-opacity, 1)) !important
}

.link-primary {
    color: RGBA(var(--mdb-primary-rgb), var(--mdb-link-opacity, 1)) !important;
    text-decoration-color: RGBA(var(--mdb-primary-rgb), var(--mdb-link-underline-opacity, 1)) !important
}

.link-primary:hover,
.link-primary:focus {
    color: RGBA(56, 107, 192, var(--mdb-link-opacity, 1)) !important;
    text-decoration-color: RGBA(56, 107, 192, var(--mdb-link-underline-opacity, 1)) !important
}

.link-secondary {
    color: RGBA(var(--mdb-secondary-rgb), var(--mdb-link-opacity, 1)) !important;
    text-decoration-color: RGBA(var(--mdb-secondary-rgb), var(--mdb-link-underline-opacity, 1)) !important
}

.link-secondary:hover,
.link-secondary:focus {
    color: RGBA(151, 158, 169, var(--mdb-link-opacity, 1)) !important;
    text-decoration-color: RGBA(151, 158, 169, var(--mdb-link-underline-opacity, 1)) !important
}

.link-success {
    color: RGBA(var(--mdb-success-rgb), var(--mdb-link-opacity, 1)) !important;
    text-decoration-color: RGBA(var(--mdb-success-rgb), var(--mdb-link-underline-opacity, 1)) !important
}

.link-success:hover,
.link-success:focus {
    color: RGBA(19, 156, 73, var(--mdb-link-opacity, 1)) !important;
    text-decoration-color: RGBA(19, 156, 73, var(--mdb-link-underline-opacity, 1)) !important
}

.link-danger {
    color: RGBA(var(--mdb-danger-rgb), var(--mdb-link-opacity, 1)) !important;
    text-decoration-color: RGBA(var(--mdb-danger-rgb), var(--mdb-link-underline-opacity, 1)) !important
}

.link-danger:hover,
.link-danger:focus {
    color: RGBA(209, 72, 95, var(--mdb-link-opacity, 1)) !important;
    text-decoration-color: RGBA(209, 72, 95, var(--mdb-link-underline-opacity, 1)) !important
}

.link-warning {
    color: RGBA(var(--mdb-warning-rgb), var(--mdb-link-opacity, 1)) !important;
    text-decoration-color: RGBA(var(--mdb-warning-rgb), var(--mdb-link-underline-opacity, 1)) !important
}

.link-warning:hover,
.link-warning:focus {
    color: RGBA(217, 153, 26, var(--mdb-link-opacity, 1)) !important;
    text-decoration-color: RGBA(217, 153, 26, var(--mdb-link-underline-opacity, 1)) !important
}

.link-info {
    color: RGBA(var(--mdb-info-rgb), var(--mdb-link-opacity, 1)) !important;
    text-decoration-color: RGBA(var(--mdb-info-rgb), var(--mdb-link-underline-opacity, 1)) !important
}

.link-info:hover,
.link-info:focus {
    color: RGBA(80, 171, 200, var(--mdb-link-opacity, 1)) !important;
    text-decoration-color: RGBA(80, 171, 200, var(--mdb-link-underline-opacity, 1)) !important
}

.link-light {
    color: RGBA(var(--mdb-light-rgb), var(--mdb-link-opacity, 1)) !important;
    text-decoration-color: RGBA(var(--mdb-light-rgb), var(--mdb-link-underline-opacity, 1)) !important
}

.link-light:hover,
.link-light:focus {
    color: RGBA(251, 251, 251, var(--mdb-link-opacity, 1)) !important;
    text-decoration-color: RGBA(251, 251, 251, var(--mdb-link-underline-opacity, 1)) !important
}

.link-dark {
    color: RGBA(var(--mdb-dark-rgb), var(--mdb-link-opacity, 1)) !important;
    text-decoration-color: RGBA(var(--mdb-dark-rgb), var(--mdb-link-underline-opacity, 1)) !important
}

.link-dark:hover,
.link-dark:focus {
    color: RGBA(48, 43, 43, var(--mdb-link-opacity, 1)) !important;
    text-decoration-color: RGBA(48, 43, 43, var(--mdb-link-underline-opacity, 1)) !important
}

.link-body-emphasis {
    color: RGBA(var(--mdb-emphasis-color-rgb), var(--mdb-link-opacity, 1)) !important;
    text-decoration-color: RGBA(var(--mdb-emphasis-color-rgb), var(--mdb-link-underline-opacity, 1)) !important
}

.link-body-emphasis:hover,
.link-body-emphasis:focus {
    color: RGBA(var(--mdb-emphasis-color-rgb), var(--mdb-link-opacity, 0.75)) !important;
    text-decoration-color: RGBA(var(--mdb-emphasis-color-rgb), var(--mdb-link-underline-opacity, 0.75)) !important
}

.focus-ring:focus {
    outline: 0;
    box-shadow: var(--mdb-focus-ring-x, 0) var(--mdb-focus-ring-y, 0) var(--mdb-focus-ring-blur, 0) var(--mdb-focus-ring-width) var(--mdb-focus-ring-color)
}

.icon-link {
    display: inline-flex;
    gap: .375rem;
    align-items: center;
    text-decoration-color: rgba(var(--mdb-link-color-rgb), var(--mdb-link-opacity, 0.5));
    text-underline-offset: .25em;
    backface-visibility: hidden
}

.icon-link>.bi {
    flex-shrink: 0;
    width: 1em;
    height: 1em;
    fill: currentcolor;
    transition: .2s ease-in-out transform
}

@media(prefers-reduced-motion: reduce) {
    .icon-link>.bi {
        transition: none
    }
}

.icon-link-hover:hover>.bi,
.icon-link-hover:focus-visible>.bi {
    transform: var(--mdb-icon-link-transform, translate3d(0.25em, 0, 0))
}

.ratio {
    position: relative;
    width: 100%
}

.ratio::before {
    display: block;
    padding-top: var(--mdb-aspect-ratio);
    content: ""
}

.ratio>* {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%
}

.ratio-1x1 {
    --mdb-aspect-ratio: 100%
}

.ratio-4x3 {
    --mdb-aspect-ratio: 75%
}

.ratio-16x9 {
    --mdb-aspect-ratio: 56.25%
}

.ratio-21x9 {
    --mdb-aspect-ratio: 42.8571428571%
}

.fixed-top {
    position: fixed;
    top: 0;
    right: 0;
    left: 0;
    z-index: 1030
}

.fixed-bottom {
    position: fixed;
    right: 0;
    bottom: 0;
    left: 0;
    z-index: 1030
}

.sticky-top {
    position: sticky;
    top: 0;
    z-index: 1020
}

.sticky-bottom {
    position: sticky;
    bottom: 0;
    z-index: 1020
}

@media(min-width: 576px) {
    .sticky-sm-top {
        position: sticky;
        top: 0;
        z-index: 1020
    }

    .sticky-sm-bottom {
        position: sticky;
        bottom: 0;
        z-index: 1020
    }
}

@media(min-width: 768px) {
    .sticky-md-top {
        position: sticky;
        top: 0;
        z-index: 1020
    }

    .sticky-md-bottom {
        position: sticky;
        bottom: 0;
        z-index: 1020
    }
}

@media(min-width: 992px) {
    .sticky-lg-top {
        position: sticky;
        top: 0;
        z-index: 1020
    }

    .sticky-lg-bottom {
        position: sticky;
        bottom: 0;
        z-index: 1020
    }
}

@media(min-width: 1200px) {
    .sticky-xl-top {
        position: sticky;
        top: 0;
        z-index: 1020
    }

    .sticky-xl-bottom {
        position: sticky;
        bottom: 0;
        z-index: 1020
    }
}

@media(min-width: 1400px) {
    .sticky-xxl-top {
        position: sticky;
        top: 0;
        z-index: 1020
    }

    .sticky-xxl-bottom {
        position: sticky;
        bottom: 0;
        z-index: 1020
    }
}

.hstack {
    display: flex;
    flex-direction: row;
    align-items: center;
    align-self: stretch
}

.vstack {
    display: flex;
    flex: 1 1 auto;
    flex-direction: column;
    align-self: stretch
}

.visually-hidden,
.visually-hidden-focusable:not(:focus):not(:focus-within) {
    width: 1px !important;
    height: 1px !important;
    padding: 0 !important;
    margin: -1px !important;
    overflow: hidden !important;
    clip: rect(0, 0, 0, 0) !important;
    white-space: nowrap !important;
    border: 0 !important
}

.visually-hidden:not(caption),
.visually-hidden-focusable:not(:focus):not(:focus-within):not(caption) {
    position: absolute !important
}

.stretched-link::after {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    z-index: 1;
    content: ""
}

.text-truncate {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap
}

.vr {
    display: inline-block;
    align-self: stretch;
    width: var(--mdb-border-width);
    min-height: 1em;
    background-color: currentcolor;
    opacity: .25
}

.diagonal-fractions {
    font-variant-numeric: diagonal-fractions
}

.bg-super-light {
    --mdb-bg-super-light: #fbfbfb;
    background-color: var(--mdb-bg-super-light)
}

.bg-fixed {
    background-attachment: fixed
}

.bg-local {
    background-attachment: local
}

.bg-scroll {
    background-attachment: scroll
}

.overflow-y-scroll {
    overflow-y: scroll
}

.overflow-x-scroll {
    overflow-x: scroll
}

.table-fixed {
    table-layout: fixed
}

.table-auto {
    table-layout: auto
}

.link-primary {
    transition: color .15s
}

.link-secondary {
    transition: color .15s
}

.link-success {
    transition: color .15s
}

.link-danger {
    transition: color .15s
}

.link-warning {
    transition: color .15s
}

.link-info {
    transition: color .15s
}

.link-light {
    transition: color .15s
}

.link-dark {
    transition: color .15s
}

.align-baseline {
    vertical-align: baseline !important
}

.align-top {
    vertical-align: top !important
}

.align-middle {
    vertical-align: middle !important
}

.align-bottom {
    vertical-align: bottom !important
}

.align-text-bottom {
    vertical-align: text-bottom !important
}

.align-text-top {
    vertical-align: text-top !important
}

.float-start {
    float: left !important
}

.float-end {
    float: right !important
}

.float-none {
    float: none !important
}

.object-cover {
    object-fit: cover !important
}

.opacity-0 {
    opacity: 0 !important
}

.opacity-5 {
    opacity: .05 !important
}

.opacity-10 {
    opacity: .1 !important
}

.opacity-15 {
    opacity: .15 !important
}

.opacity-20 {
    opacity: .2 !important
}

.opacity-25 {
    opacity: .25 !important
}

.opacity-30 {
    opacity: .3 !important
}

.opacity-35 {
    opacity: .35 !important
}

.opacity-40 {
    opacity: .4 !important
}

.opacity-45 {
    opacity: .45 !important
}

.opacity-50 {
    opacity: .5 !important
}

.opacity-55 {
    opacity: .55 !important
}

.opacity-60 {
    opacity: .6 !important
}

.opacity-65 {
    opacity: .65 !important
}

.opacity-70 {
    opacity: .7 !important
}

.opacity-75 {
    opacity: .75 !important
}

.opacity-80 {
    opacity: .8 !important
}

.opacity-85 {
    opacity: .85 !important
}

.opacity-90 {
    opacity: .9 !important
}

.opacity-95 {
    opacity: .95 !important
}

.opacity-100 {
    opacity: 1 !important
}

.overflow-auto {
    overflow: auto !important
}

.overflow-hidden {
    overflow: hidden !important
}

.overflow-visible {
    overflow: visible !important
}

.overflow-scroll {
    overflow: scroll !important
}

.overflow-x-auto {
    overflow-x: auto !important
}

.overflow-x-hidden {
    overflow-x: hidden !important
}

.overflow-x-visible {
    overflow-x: visible !important
}

.overflow-x-scroll {
    overflow-x: scroll !important
}

.overflow-y-auto {
    overflow-y: auto !important
}

.overflow-y-hidden {
    overflow-y: hidden !important
}

.overflow-y-visible {
    overflow-y: visible !important
}

.overflow-y-scroll {
    overflow-y: scroll !important
}

.d-inline {
    display: inline !important
}

.d-inline-block {
    display: inline-block !important
}

.d-block {
    display: block !important
}

.d-grid {
    display: grid !important
}

.d-inline-grid {
    display: inline-grid !important
}

.d-table {
    display: table !important
}

.d-table-row {
    display: table-row !important
}

.d-table-cell {
    display: table-cell !important
}

.d-flex {
    display: flex !important
}

.d-inline-flex {
    display: inline-flex !important
}

.d-none {
    display: none !important
}

.shadow {
    box-shadow: var(--mdb-box-shadow) !important
}

.shadow-sm {
    box-shadow: var(--mdb-box-shadow-sm) !important
}

.shadow-lg {
    box-shadow: var(--mdb-box-shadow-lg) !important
}

.shadow-none {
    box-shadow: none !important
}

.shadow-0 {
    box-shadow: none !important
}

.shadow-1 {
    box-shadow: 0 0px 2px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.07), 0 1px 1px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.04) !important
}

.shadow-2 {
    box-shadow: 0 0px 3px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.07), 0 2px 2px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.04) !important
}

.shadow-3 {
    box-shadow: 0 2px 6px -1px rgba(var(--mdb-box-shadow-color-rgb), 0.07), 0 6px 18px -1px rgba(var(--mdb-box-shadow-color-rgb), 0.04) !important
}

.shadow-4 {
    box-shadow: 0 2px 15px -3px rgba(var(--mdb-box-shadow-color-rgb), 0.07), 0 10px 20px -2px rgba(var(--mdb-box-shadow-color-rgb), 0.04) !important
}

.shadow-5 {
    box-shadow: 0 2px 25px -5px rgba(var(--mdb-box-shadow-color-rgb), 0.07), 0 25px 21px -5px rgba(var(--mdb-box-shadow-color-rgb), 0.04) !important
}

.shadow-6 {
    box-shadow: 0 2px 35px -12px rgba(var(--mdb-box-shadow-color-rgb), 0.21), 0 50px 40px -5px rgba(var(--mdb-box-shadow-color-rgb), 0.04) !important
}

.shadow-1-soft {
    box-shadow: 0 1px 5px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.05) !important
}

.shadow-2-soft {
    box-shadow: 0 2px 10px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.05) !important
}

.shadow-3-soft {
    box-shadow: 0 5px 15px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.05) !important
}

.shadow-4-soft {
    box-shadow: 0 10px 20px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.05) !important
}

.shadow-5-soft {
    box-shadow: 0 15px 30px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.05) !important
}

.shadow-6-soft {
    box-shadow: 0 20px 40px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.05) !important
}

.shadow-1-strong {
    box-shadow: 0 0px 2px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.16), 0 1px 1px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1) !important
}

.shadow-2-strong {
    box-shadow: 0 0px 3px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.16), 0 2px 2px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1) !important
}

.shadow-3-strong {
    box-shadow: 0 2px 6px -1px rgba(var(--mdb-box-shadow-color-rgb), 0.16), 0 6px 18px -1px rgba(var(--mdb-box-shadow-color-rgb), 0.1) !important
}

.shadow-4-strong {
    box-shadow: 0 2px 15px -3px rgba(var(--mdb-box-shadow-color-rgb), 0.16), 0 10px 20px -2px rgba(var(--mdb-box-shadow-color-rgb), 0.1) !important
}

.shadow-5-strong {
    box-shadow: 0 2px 25px -5px rgba(var(--mdb-box-shadow-color-rgb), 0.16), 0 25px 21px -5px rgba(var(--mdb-box-shadow-color-rgb), 0.1) !important
}

.shadow-6-strong {
    box-shadow: 0 2px 35px -12px rgba(var(--mdb-box-shadow-color-rgb), 0.26), 0 50px 40px -5px rgba(var(--mdb-box-shadow-color-rgb), 0.1) !important
}

.shadow-inner {
    box-shadow: inset 0 2px 4px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.06) !important
}

.focus-ring-primary {
    --mdb-focus-ring-color: rgba(var(--mdb-primary-rgb), var(--mdb-focus-ring-opacity))
}

.focus-ring-secondary {
    --mdb-focus-ring-color: rgba(var(--mdb-secondary-rgb), var(--mdb-focus-ring-opacity))
}

.focus-ring-success {
    --mdb-focus-ring-color: rgba(var(--mdb-success-rgb), var(--mdb-focus-ring-opacity))
}

.focus-ring-danger {
    --mdb-focus-ring-color: rgba(var(--mdb-danger-rgb), var(--mdb-focus-ring-opacity))
}

.focus-ring-warning {
    --mdb-focus-ring-color: rgba(var(--mdb-warning-rgb), var(--mdb-focus-ring-opacity))
}

.focus-ring-info {
    --mdb-focus-ring-color: rgba(var(--mdb-info-rgb), var(--mdb-focus-ring-opacity))
}

.focus-ring-light {
    --mdb-focus-ring-color: rgba(var(--mdb-light-rgb), var(--mdb-focus-ring-opacity))
}

.focus-ring-dark {
    --mdb-focus-ring-color: rgba(var(--mdb-dark-rgb), var(--mdb-focus-ring-opacity))
}

.position-static {
    position: static !important
}

.position-relative {
    position: relative !important
}

.position-absolute {
    position: absolute !important
}

.position-fixed {
    position: fixed !important
}

.position-sticky {
    position: sticky !important
}

.top-0 {
    top: 0 !important
}

.top-50 {
    top: 50% !important
}

.top-100 {
    top: 100% !important
}

.bottom-0 {
    bottom: 0 !important
}

.bottom-50 {
    bottom: 50% !important
}

.bottom-100 {
    bottom: 100% !important
}

.start-0 {
    left: 0 !important
}

.start-50 {
    left: 50% !important
}

.start-100 {
    left: 100% !important
}

.end-0 {
    right: 0 !important
}

.end-50 {
    right: 50% !important
}

.end-100 {
    right: 100% !important
}

.translate-middle {
    transform: translate(-50%, -50%) !important
}

.translate-middle-x {
    transform: translateX(-50%) !important
}

.translate-middle-y {
    transform: translateY(-50%) !important
}

.border {
    border: var(--mdb-border-width) var(--mdb-border-style) var(--mdb-border-color) !important
}

.border-0 {
    border: 0 !important
}

.border-top {
    border-top: var(--mdb-border-width) var(--mdb-border-style) var(--mdb-border-color) !important
}

.border-top-0 {
    border-top: 0 !important
}

.border-end {
    border-right: var(--mdb-border-width) var(--mdb-border-style) var(--mdb-border-color) !important
}

.border-end-0 {
    border-right: 0 !important
}

.border-bottom {
    border-bottom: var(--mdb-border-width) var(--mdb-border-style) var(--mdb-border-color) !important
}

.border-bottom-0 {
    border-bottom: 0 !important
}

.border-start {
    border-left: var(--mdb-border-width) var(--mdb-border-style) var(--mdb-border-color) !important
}

.border-start-0 {
    border-left: 0 !important
}

.border-primary {
    --mdb-border-opacity: 1;
    border-color: rgba(var(--mdb-primary-rgb), var(--mdb-border-opacity)) !important
}

.border-secondary {
    --mdb-border-opacity: 1;
    border-color: rgba(var(--mdb-secondary-rgb), var(--mdb-border-opacity)) !important
}

.border-success {
    --mdb-border-opacity: 1;
    border-color: rgba(var(--mdb-success-rgb), var(--mdb-border-opacity)) !important
}

.border-danger {
    --mdb-border-opacity: 1;
    border-color: rgba(var(--mdb-danger-rgb), var(--mdb-border-opacity)) !important
}

.border-warning {
    --mdb-border-opacity: 1;
    border-color: rgba(var(--mdb-warning-rgb), var(--mdb-border-opacity)) !important
}

.border-info {
    --mdb-border-opacity: 1;
    border-color: rgba(var(--mdb-info-rgb), var(--mdb-border-opacity)) !important
}

.border-light {
    --mdb-border-opacity: 1;
    border-color: rgba(var(--mdb-light-rgb), var(--mdb-border-opacity)) !important
}

.border-dark {
    --mdb-border-opacity: 1;
    border-color: rgba(var(--mdb-dark-rgb), var(--mdb-border-opacity)) !important
}

.border-black {
    --mdb-border-opacity: 1;
    border-color: rgba(var(--mdb-black-rgb), var(--mdb-border-opacity)) !important
}

.border-white {
    --mdb-border-opacity: 1;
    border-color: rgba(var(--mdb-white-rgb), var(--mdb-border-opacity)) !important
}

.border-primary-subtle {
    border-color: var(--mdb-primary-border-subtle) !important
}

.border-secondary-subtle {
    border-color: var(--mdb-secondary-border-subtle) !important
}

.border-success-subtle {
    border-color: var(--mdb-success-border-subtle) !important
}

.border-info-subtle {
    border-color: var(--mdb-info-border-subtle) !important
}

.border-warning-subtle {
    border-color: var(--mdb-warning-border-subtle) !important
}

.border-danger-subtle {
    border-color: var(--mdb-danger-border-subtle) !important
}

.border-light-subtle {
    border-color: var(--mdb-light-border-subtle) !important
}

.border-dark-subtle {
    border-color: var(--mdb-dark-border-subtle) !important
}

.border-1 {
    border-width: 1px !important
}

.border-2 {
    border-width: 2px !important
}

.border-3 {
    border-width: 3px !important
}

.border-4 {
    border-width: 4px !important
}

.border-5 {
    border-width: 5px !important
}

.border-opacity-10 {
    --mdb-border-opacity: 0.1
}

.border-opacity-25 {
    --mdb-border-opacity: 0.25
}

.border-opacity-50 {
    --mdb-border-opacity: 0.5
}

.border-opacity-75 {
    --mdb-border-opacity: 0.75
}

.border-opacity-100 {
    --mdb-border-opacity: 1
}

.w-25 {
    width: 25% !important
}

.w-50 {
    width: 50% !important
}

.w-75 {
    width: 75% !important
}

.w-100 {
    width: 100% !important
}

.w-auto {
    width: auto !important
}

.mw-100 {
    max-width: 100% !important
}

.vw-100 {
    width: 100vw !important
}

.min-vw-100 {
    min-width: 100vw !important
}

.h-25 {
    height: 25% !important
}

.h-50 {
    height: 50% !important
}

.h-75 {
    height: 75% !important
}

.h-100 {
    height: 100% !important
}

.h-auto {
    height: auto !important
}

.mh-100 {
    max-height: 100% !important
}

.vh-100 {
    height: 100vh !important
}

.min-vh-100 {
    min-height: 100vh !important
}

.flex-fill {
    flex: 1 1 auto !important
}

.flex-row {
    flex-direction: row !important
}

.flex-column {
    flex-direction: column !important
}

.flex-row-reverse {
    flex-direction: row-reverse !important
}

.flex-column-reverse {
    flex-direction: column-reverse !important
}

.flex-grow-0 {
    flex-grow: 0 !important
}

.flex-grow-1 {
    flex-grow: 1 !important
}

.flex-shrink-0 {
    flex-shrink: 0 !important
}

.flex-shrink-1 {
    flex-shrink: 1 !important
}

.flex-wrap {
    flex-wrap: wrap !important
}

.flex-nowrap {
    flex-wrap: nowrap !important
}

.flex-wrap-reverse {
    flex-wrap: wrap-reverse !important
}

.justify-content-start {
    justify-content: flex-start !important
}

.justify-content-end {
    justify-content: flex-end !important
}

.justify-content-center {
    justify-content: center !important
}

.justify-content-between {
    justify-content: space-between !important
}

.justify-content-around {
    justify-content: space-around !important
}

.justify-content-evenly {
    justify-content: space-evenly !important
}

.align-items-start {
    align-items: flex-start !important
}

.align-items-end {
    align-items: flex-end !important
}

.align-items-center {
    align-items: center !important
}

.align-items-baseline {
    align-items: baseline !important
}

.align-items-stretch {
    align-items: stretch !important
}

.align-content-start {
    align-content: flex-start !important
}

.align-content-end {
    align-content: flex-end !important
}

.align-content-center {
    align-content: center !important
}

.align-content-between {
    align-content: space-between !important
}

.align-content-around {
    align-content: space-around !important
}

.align-content-stretch {
    align-content: stretch !important
}

.align-self-auto {
    align-self: auto !important
}

.align-self-start {
    align-self: flex-start !important
}

.align-self-end {
    align-self: flex-end !important
}

.align-self-center {
    align-self: center !important
}

.align-self-baseline {
    align-self: baseline !important
}

.align-self-stretch {
    align-self: stretch !important
}

.order-first {
    order: -1 !important
}

.order-0 {
    order: 0 !important
}

.order-1 {
    order: 1 !important
}

.order-2 {
    order: 2 !important
}

.order-3 {
    order: 3 !important
}

.order-4 {
    order: 4 !important
}

.order-5 {
    order: 5 !important
}

.order-last {
    order: 6 !important
}

.m-0 {
    margin: 0 !important
}

.m-1 {
    margin: .25rem !important
}

.m-2 {
    margin: .5rem !important
}

.m-3 {
    margin: 1rem !important
}

.m-4 {
    margin: 1.5rem !important
}

.m-5 {
    margin: 3rem !important
}

.m-auto {
    margin: auto !important
}

.mx-0 {
    margin-right: 0 !important;
    margin-left: 0 !important
}

.mx-1 {
    margin-right: .25rem !important;
    margin-left: .25rem !important
}

.mx-2 {
    margin-right: .5rem !important;
    margin-left: .5rem !important
}

.mx-3 {
    margin-right: 1rem !important;
    margin-left: 1rem !important
}

.mx-4 {
    margin-right: 1.5rem !important;
    margin-left: 1.5rem !important
}

.mx-5 {
    margin-right: 3rem !important;
    margin-left: 3rem !important
}

.mx-auto {
    margin-right: auto !important;
    margin-left: auto !important
}

.my-0 {
    margin-top: 0 !important;
    margin-bottom: 0 !important
}

.my-1 {
    margin-top: .25rem !important;
    margin-bottom: .25rem !important
}

.my-2 {
    margin-top: .5rem !important;
    margin-bottom: .5rem !important
}

.my-3 {
    margin-top: 1rem !important;
    margin-bottom: 1rem !important
}

.my-4 {
    margin-top: 1.5rem !important;
    margin-bottom: 1.5rem !important
}

.my-5 {
    margin-top: 3rem !important;
    margin-bottom: 3rem !important
}

.my-auto {
    margin-top: auto !important;
    margin-bottom: auto !important
}

.mt-0 {
    margin-top: 0 !important
}

.mt-1 {
    margin-top: .25rem !important
}

.mt-2 {
    margin-top: .5rem !important
}

.mt-3 {
    margin-top: 1rem !important
}

.mt-4 {
    margin-top: 1.5rem !important
}

.mt-5 {
    margin-top: 3rem !important
}

.mt-auto {
    margin-top: auto !important
}

.me-0 {
    margin-right: 0 !important
}

.me-1 {
    margin-right: .25rem !important
}

.me-2 {
    margin-right: .5rem !important
}

.me-3 {
    margin-right: 1rem !important
}

.me-4 {
    margin-right: 1.5rem !important
}

.me-5 {
    margin-right: 3rem !important
}

.me-auto {
    margin-right: auto !important
}

.mb-0 {
    margin-bottom: 0 !important
}

.mb-1 {
    margin-bottom: .25rem !important
}

.mb-2 {
    margin-bottom: .5rem !important
}

.mb-3 {
    margin-bottom: 1rem !important
}

.mb-4 {
    margin-bottom: 1.5rem !important
}

.mb-5 {
    margin-bottom: 3rem !important
}

.mb-auto {
    margin-bottom: auto !important
}

.mb-6 {
    margin-bottom: 3.5rem !important
}

.mb-7 {
    margin-bottom: 4rem !important
}

.mb-8 {
    margin-bottom: 5rem !important
}

.mb-9 {
    margin-bottom: 6rem !important
}

.mb-10 {
    margin-bottom: 8rem !important
}

.mb-11 {
    margin-bottom: 10rem !important
}

.mb-12 {
    margin-bottom: 12rem !important
}

.mb-13 {
    margin-bottom: 14rem !important
}

.mb-14 {
    margin-bottom: 16rem !important
}

.ms-0 {
    margin-left: 0 !important
}

.ms-1 {
    margin-left: .25rem !important
}

.ms-2 {
    margin-left: .5rem !important
}

.ms-3 {
    margin-left: 1rem !important
}

.ms-4 {
    margin-left: 1.5rem !important
}

.ms-5 {
    margin-left: 3rem !important
}

.ms-auto {
    margin-left: auto !important
}

.m-n1 {
    margin: -0.25rem !important
}

.m-n2 {
    margin: -0.5rem !important
}

.m-n3 {
    margin: -1rem !important
}

.m-n4 {
    margin: -1.5rem !important
}

.m-n5 {
    margin: -3rem !important
}

.mx-n1 {
    margin-right: -0.25rem !important;
    margin-left: -0.25rem !important
}

.mx-n2 {
    margin-right: -0.5rem !important;
    margin-left: -0.5rem !important
}

.mx-n3 {
    margin-right: -1rem !important;
    margin-left: -1rem !important
}

.mx-n4 {
    margin-right: -1.5rem !important;
    margin-left: -1.5rem !important
}

.mx-n5 {
    margin-right: -3rem !important;
    margin-left: -3rem !important
}

.my-n1 {
    margin-top: -0.25rem !important;
    margin-bottom: -0.25rem !important
}

.my-n2 {
    margin-top: -0.5rem !important;
    margin-bottom: -0.5rem !important
}

.my-n3 {
    margin-top: -1rem !important;
    margin-bottom: -1rem !important
}

.my-n4 {
    margin-top: -1.5rem !important;
    margin-bottom: -1.5rem !important
}

.my-n5 {
    margin-top: -3rem !important;
    margin-bottom: -3rem !important
}

.mt-n1 {
    margin-top: -0.25rem !important
}

.mt-n2 {
    margin-top: -0.5rem !important
}

.mt-n3 {
    margin-top: -1rem !important
}

.mt-n4 {
    margin-top: -1.5rem !important
}

.mt-n5 {
    margin-top: -3rem !important
}

.me-n1 {
    margin-right: -0.25rem !important
}

.me-n2 {
    margin-right: -0.5rem !important
}

.me-n3 {
    margin-right: -1rem !important
}

.me-n4 {
    margin-right: -1.5rem !important
}

.me-n5 {
    margin-right: -3rem !important
}

.mb-n1 {
    margin-bottom: -0.25rem !important
}

.mb-n2 {
    margin-bottom: -0.5rem !important
}

.mb-n3 {
    margin-bottom: -1rem !important
}

.mb-n4 {
    margin-bottom: -1.5rem !important
}

.mb-n5 {
    margin-bottom: -3rem !important
}

.ms-n1 {
    margin-left: -0.25rem !important
}

.ms-n2 {
    margin-left: -0.5rem !important
}

.ms-n3 {
    margin-left: -1rem !important
}

.ms-n4 {
    margin-left: -1.5rem !important
}

.ms-n5 {
    margin-left: -3rem !important
}

.p-0 {
    padding: 0 !important
}

.p-1 {
    padding: .25rem !important
}

.p-2 {
    padding: .5rem !important
}

.p-3 {
    padding: 1rem !important
}

.p-4 {
    padding: 1.5rem !important
}

.p-5 {
    padding: 3rem !important
}

.px-0 {
    padding-right: 0 !important;
    padding-left: 0 !important
}

.px-1 {
    padding-right: .25rem !important;
    padding-left: .25rem !important
}

.px-2 {
    padding-right: .5rem !important;
    padding-left: .5rem !important
}

.px-3 {
    padding-right: 1rem !important;
    padding-left: 1rem !important
}

.px-4 {
    padding-right: 1.5rem !important;
    padding-left: 1.5rem !important
}

.px-5 {
    padding-right: 3rem !important;
    padding-left: 3rem !important
}

.py-0 {
    padding-top: 0 !important;
    padding-bottom: 0 !important
}

.py-1 {
    padding-top: .25rem !important;
    padding-bottom: .25rem !important
}

.py-2 {
    padding-top: .5rem !important;
    padding-bottom: .5rem !important
}

.py-3 {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important
}

.py-4 {
    padding-top: 1.5rem !important;
    padding-bottom: 1.5rem !important
}

.py-5 {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important
}

.pt-0 {
    padding-top: 0 !important
}

.pt-1 {
    padding-top: .25rem !important
}

.pt-2 {
    padding-top: .5rem !important
}

.pt-3 {
    padding-top: 1rem !important
}

.pt-4 {
    padding-top: 1.5rem !important
}

.pt-5 {
    padding-top: 3rem !important
}

.pe-0 {
    padding-right: 0 !important
}

.pe-1 {
    padding-right: .25rem !important
}

.pe-2 {
    padding-right: .5rem !important
}

.pe-3 {
    padding-right: 1rem !important
}

.pe-4 {
    padding-right: 1.5rem !important
}

.pe-5 {
    padding-right: 3rem !important
}

.pb-0 {
    padding-bottom: 0 !important
}

.pb-1 {
    padding-bottom: .25rem !important
}

.pb-2 {
    padding-bottom: .5rem !important
}

.pb-3 {
    padding-bottom: 1rem !important
}

.pb-4 {
    padding-bottom: 1.5rem !important
}

.pb-5 {
    padding-bottom: 3rem !important
}

.ps-0 {
    padding-left: 0 !important
}

.ps-1 {
    padding-left: .25rem !important
}

.ps-2 {
    padding-left: .5rem !important
}

.ps-3 {
    padding-left: 1rem !important
}

.ps-4 {
    padding-left: 1.5rem !important
}

.ps-5 {
    padding-left: 3rem !important
}

.gap-0 {
    gap: 0 !important
}

.gap-1 {
    gap: .25rem !important
}

.gap-2 {
    gap: .5rem !important
}

.gap-3 {
    gap: 1rem !important
}

.gap-4 {
    gap: 1.5rem !important
}

.gap-5 {
    gap: 3rem !important
}

.row-gap-0 {
    row-gap: 0 !important
}

.row-gap-1 {
    row-gap: .25rem !important
}

.row-gap-2 {
    row-gap: .5rem !important
}

.row-gap-3 {
    row-gap: 1rem !important
}

.row-gap-4 {
    row-gap: 1.5rem !important
}

.row-gap-5 {
    row-gap: 3rem !important
}

.column-gap-0 {
    column-gap: 0 !important
}

.column-gap-1 {
    column-gap: .25rem !important
}

.column-gap-2 {
    column-gap: .5rem !important
}

.column-gap-3 {
    column-gap: 1rem !important
}

.column-gap-4 {
    column-gap: 1.5rem !important
}

.column-gap-5 {
    column-gap: 3rem !important
}

.font-monospace {
    font-family: var(--mdb-font-monospace) !important
}

.fs-1 {
    font-size: calc(1.375rem + 1.5vw) !important
}

.fs-2 {
    font-size: calc(1.325rem + 0.9vw) !important
}

.fs-3 {
    font-size: calc(1.3rem + 0.6vw) !important
}

.fs-4 {
    font-size: calc(1.275rem + 0.3vw) !important
}

.fs-5 {
    font-size: 1.25rem !important
}

.fs-6 {
    font-size: 1rem !important
}

.fst-italic {
    font-style: italic !important
}

.fst-normal {
    font-style: normal !important
}

.fw-lighter {
    font-weight: lighter !important
}

.fw-light {
    font-weight: 300 !important
}

.fw-normal {
    font-weight: 400 !important
}

.fw-medium {
    font-weight: 500 !important
}

.fw-semibold {
    font-weight: 600 !important
}

.fw-bold {
    font-weight: 700 !important
}

.fw-bolder {
    font-weight: bolder !important
}

.lh-1 {
    line-height: 1 !important
}

.lh-sm {
    line-height: 1.25 !important
}

.lh-base {
    line-height: 1.6 !important
}

.lh-lg {
    line-height: 2 !important
}

.text-start {
    text-align: left !important
}

.text-end {
    text-align: right !important
}

.text-center {
    text-align: center !important
}

.text-decoration-none {
    text-decoration: none !important
}

.text-decoration-underline {
    text-decoration: underline !important
}

.text-decoration-line-through {
    text-decoration: line-through !important
}

.text-lowercase {
    text-transform: lowercase !important
}

.text-uppercase {
    text-transform: uppercase !important
}

.text-capitalize {
    text-transform: capitalize !important
}

.text-wrap {
    white-space: normal !important
}

.text-nowrap {
    white-space: nowrap !important
}

.text-break {
    word-wrap: break-word !important;
    word-break: break-word !important
}

.text-primary {
    --mdb-text-opacity: 1;
    color: rgba(var(--mdb-primary-rgb), var(--mdb-text-opacity)) !important
}

.text-secondary {
    --mdb-text-opacity: 1;
    color: rgba(var(--mdb-secondary-rgb), var(--mdb-text-opacity)) !important
}

.text-success {
    --mdb-text-opacity: 1;
    color: rgba(var(--mdb-success-rgb), var(--mdb-text-opacity)) !important
}

.text-danger {
    --mdb-text-opacity: 1;
    color: rgba(var(--mdb-danger-rgb), var(--mdb-text-opacity)) !important
}

.text-warning {
    --mdb-text-opacity: 1;
    color: rgba(var(--mdb-warning-rgb), var(--mdb-text-opacity)) !important
}

.text-info {
    --mdb-text-opacity: 1;
    color: rgba(var(--mdb-info-rgb), var(--mdb-text-opacity)) !important
}

.text-light {
    --mdb-text-opacity: 1;
    color: rgba(var(--mdb-light-rgb), var(--mdb-text-opacity)) !important
}

.text-dark {
    --mdb-text-opacity: 1;
    color: rgba(var(--mdb-dark-rgb), var(--mdb-text-opacity)) !important
}

.text-black {
    --mdb-text-opacity: 1;
    color: rgba(var(--mdb-black-rgb), var(--mdb-text-opacity)) !important
}

.text-white {
    --mdb-text-opacity: 1;
    color: rgba(var(--mdb-white-rgb), var(--mdb-text-opacity)) !important
}

.text-body {
    --mdb-text-opacity: 1;
    color: rgba(var(--mdb-body-color-rgb), var(--mdb-text-opacity)) !important
}

.text-muted {
    --mdb-text-opacity: 1;
    color: var(--mdb-secondary-color) !important
}

.text-black-50 {
    --mdb-text-opacity: 1;
    color: rgba(0, 0, 0, .5) !important
}

.text-white-50 {
    --mdb-text-opacity: 1;
    color: rgba(255, 255, 255, .5) !important
}

.text-body-secondary {
    --mdb-text-opacity: 1;
    color: var(--mdb-secondary-color) !important
}

.text-body-tertiary {
    --mdb-text-opacity: 1;
    color: var(--mdb-tertiary-color) !important
}

.text-body-emphasis {
    --mdb-text-opacity: 1;
    color: var(--mdb-emphasis-color) !important
}

.text-reset {
    --mdb-text-opacity: 1;
    color: inherit !important
}

.text-opacity-25 {
    --mdb-text-opacity: 0.25
}

.text-opacity-50 {
    --mdb-text-opacity: 0.5
}

.text-opacity-75 {
    --mdb-text-opacity: 0.75
}

.text-opacity-100 {
    --mdb-text-opacity: 1
}

.text-primary-emphasis {
    color: var(--mdb-primary-text-emphasis) !important
}

.text-secondary-emphasis {
    color: var(--mdb-secondary-text-emphasis) !important
}

.text-success-emphasis {
    color: var(--mdb-success-text-emphasis) !important
}

.text-info-emphasis {
    color: var(--mdb-info-text-emphasis) !important
}

.text-warning-emphasis {
    color: var(--mdb-warning-text-emphasis) !important
}

.text-danger-emphasis {
    color: var(--mdb-danger-text-emphasis) !important
}

.text-light-emphasis {
    color: var(--mdb-light-text-emphasis) !important
}

.text-dark-emphasis {
    color: var(--mdb-dark-text-emphasis) !important
}

.link-opacity-10 {
    --mdb-link-opacity: 0.1
}

.link-opacity-10-hover:hover {
    --mdb-link-opacity: 0.1
}

.link-opacity-25 {
    --mdb-link-opacity: 0.25
}

.link-opacity-25-hover:hover {
    --mdb-link-opacity: 0.25
}

.link-opacity-50 {
    --mdb-link-opacity: 0.5
}

.link-opacity-50-hover:hover {
    --mdb-link-opacity: 0.5
}

.link-opacity-75 {
    --mdb-link-opacity: 0.75
}

.link-opacity-75-hover:hover {
    --mdb-link-opacity: 0.75
}

.link-opacity-100 {
    --mdb-link-opacity: 1
}

.link-opacity-100-hover:hover {
    --mdb-link-opacity: 1
}

.link-offset-1 {
    text-underline-offset: .125em !important
}

.link-offset-1-hover:hover {
    text-underline-offset: .125em !important
}

.link-offset-2 {
    text-underline-offset: .25em !important
}

.link-offset-2-hover:hover {
    text-underline-offset: .25em !important
}

.link-offset-3 {
    text-underline-offset: .375em !important
}

.link-offset-3-hover:hover {
    text-underline-offset: .375em !important
}

.link-underline-primary {
    --mdb-link-underline-opacity: 1;
    text-decoration-color: rgba(var(--mdb-primary-rgb), var(--mdb-link-underline-opacity)) !important
}

.link-underline-secondary {
    --mdb-link-underline-opacity: 1;
    text-decoration-color: rgba(var(--mdb-secondary-rgb), var(--mdb-link-underline-opacity)) !important
}

.link-underline-success {
    --mdb-link-underline-opacity: 1;
    text-decoration-color: rgba(var(--mdb-success-rgb), var(--mdb-link-underline-opacity)) !important
}

.link-underline-danger {
    --mdb-link-underline-opacity: 1;
    text-decoration-color: rgba(var(--mdb-danger-rgb), var(--mdb-link-underline-opacity)) !important
}

.link-underline-warning {
    --mdb-link-underline-opacity: 1;
    text-decoration-color: rgba(var(--mdb-warning-rgb), var(--mdb-link-underline-opacity)) !important
}

.link-underline-info {
    --mdb-link-underline-opacity: 1;
    text-decoration-color: rgba(var(--mdb-info-rgb), var(--mdb-link-underline-opacity)) !important
}

.link-underline-light {
    --mdb-link-underline-opacity: 1;
    text-decoration-color: rgba(var(--mdb-light-rgb), var(--mdb-link-underline-opacity)) !important
}

.link-underline-dark {
    --mdb-link-underline-opacity: 1;
    text-decoration-color: rgba(var(--mdb-dark-rgb), var(--mdb-link-underline-opacity)) !important
}

.link-underline {
    --mdb-link-underline-opacity: 1;
    text-decoration-color: rgba(var(--mdb-link-color-rgb), var(--mdb-link-underline-opacity, 1)) !important
}

.link-underline-opacity-0 {
    --mdb-link-underline-opacity: 0
}

.link-underline-opacity-0-hover:hover {
    --mdb-link-underline-opacity: 0
}

.link-underline-opacity-10 {
    --mdb-link-underline-opacity: 0.1
}

.link-underline-opacity-10-hover:hover {
    --mdb-link-underline-opacity: 0.1
}

.link-underline-opacity-25 {
    --mdb-link-underline-opacity: 0.25
}

.link-underline-opacity-25-hover:hover {
    --mdb-link-underline-opacity: 0.25
}

.link-underline-opacity-50 {
    --mdb-link-underline-opacity: 0.5
}

.link-underline-opacity-50-hover:hover {
    --mdb-link-underline-opacity: 0.5
}

.link-underline-opacity-75 {
    --mdb-link-underline-opacity: 0.75
}

.link-underline-opacity-75-hover:hover {
    --mdb-link-underline-opacity: 0.75
}

.link-underline-opacity-100 {
    --mdb-link-underline-opacity: 1
}

.link-underline-opacity-100-hover:hover {
    --mdb-link-underline-opacity: 1
}

.bg-primary {
    --mdb-bg-opacity: 1;
    background-color: rgba(var(--mdb-primary-rgb), var(--mdb-bg-opacity)) !important
}

.bg-secondary {
    --mdb-bg-opacity: 1;
    background-color: rgba(var(--mdb-secondary-rgb), var(--mdb-bg-opacity)) !important
}

.bg-success {
    --mdb-bg-opacity: 1;
    background-color: rgba(var(--mdb-success-rgb), var(--mdb-bg-opacity)) !important
}

.bg-danger {
    --mdb-bg-opacity: 1;
    background-color: rgba(var(--mdb-danger-rgb), var(--mdb-bg-opacity)) !important
}

.bg-warning {
    --mdb-bg-opacity: 1;
    background-color: rgba(var(--mdb-warning-rgb), var(--mdb-bg-opacity)) !important
}

.bg-info {
    --mdb-bg-opacity: 1;
    background-color: rgba(var(--mdb-info-rgb), var(--mdb-bg-opacity)) !important
}

.bg-light {
    --mdb-bg-opacity: 1;
    background-color: rgba(var(--mdb-light-rgb), var(--mdb-bg-opacity)) !important
}

.bg-dark {
    --mdb-bg-opacity: 1;
    background-color: rgba(var(--mdb-dark-rgb), var(--mdb-bg-opacity)) !important
}

.bg-black {
    --mdb-bg-opacity: 1;
    background-color: rgba(var(--mdb-black-rgb), var(--mdb-bg-opacity)) !important
}

.bg-white {
    --mdb-bg-opacity: 1;
    background-color: rgba(var(--mdb-white-rgb), var(--mdb-bg-opacity)) !important
}

.bg-body {
    --mdb-bg-opacity: 1;
    background-color: rgba(var(--mdb-body-bg-rgb), var(--mdb-bg-opacity)) !important
}

.bg-transparent {
    --mdb-bg-opacity: 1;
    background-color: rgba(0, 0, 0, 0) !important
}

.bg-body-secondary {
    --mdb-bg-opacity: 1;
    background-color: rgba(var(--mdb-secondary-bg-rgb), var(--mdb-bg-opacity)) !important
}

.bg-body-tertiary {
    --mdb-bg-opacity: 1;
    background-color: rgba(var(--mdb-tertiary-bg-rgb), var(--mdb-bg-opacity)) !important
}

.bg-opacity-10 {
    --mdb-bg-opacity: 0.1
}

.bg-opacity-25 {
    --mdb-bg-opacity: 0.25
}

.bg-opacity-50 {
    --mdb-bg-opacity: 0.5
}

.bg-opacity-75 {
    --mdb-bg-opacity: 0.75
}

.bg-opacity-100 {
    --mdb-bg-opacity: 1
}

.bg-primary-subtle {
    background-color: var(--mdb-primary-bg-subtle) !important
}

.bg-secondary-subtle {
    background-color: var(--mdb-secondary-bg-subtle) !important
}

.bg-success-subtle {
    background-color: var(--mdb-success-bg-subtle) !important
}

.bg-info-subtle {
    background-color: var(--mdb-info-bg-subtle) !important
}

.bg-warning-subtle {
    background-color: var(--mdb-warning-bg-subtle) !important
}

.bg-danger-subtle {
    background-color: var(--mdb-danger-bg-subtle) !important
}

.bg-light-subtle {
    background-color: var(--mdb-light-bg-subtle) !important
}

.bg-dark-subtle {
    background-color: var(--mdb-dark-bg-subtle) !important
}

.bg-gradient {
    background-image: var(--mdb-gradient) !important
}

.user-select-all {
    user-select: all !important
}

.user-select-auto {
    user-select: auto !important
}

.user-select-none {
    user-select: none !important
}

.pe-none {
    pointer-events: none !important
}

.pe-auto {
    pointer-events: auto !important
}

.rounded {
    border-radius: var(--mdb-border-radius) !important
}

.rounded-0 {
    border-radius: 0 !important
}

.rounded-1 {
    border-radius: var(--mdb-border-radius-sm) !important
}

.rounded-2 {
    border-radius: var(--mdb-border-radius) !important
}

.rounded-3 {
    border-radius: var(--mdb-border-radius-lg) !important
}

.rounded-4 {
    border-radius: .375rem !important
}

.rounded-5 {
    border-radius: .5rem !important
}

.rounded-circle {
    border-radius: 50% !important
}

.rounded-pill {
    border-radius: var(--mdb-border-radius-pill) !important
}

.rounded-6 {
    border-radius: .75rem !important
}

.rounded-7 {
    border-radius: 1rem !important
}

.rounded-8 {
    border-radius: 1.25rem !important
}

.rounded-9 {
    border-radius: 1.5rem !important
}

.rounded-top {
    border-top-left-radius: var(--mdb-border-radius) !important;
    border-top-right-radius: var(--mdb-border-radius) !important
}

.rounded-top-0 {
    border-top-left-radius: 0 !important;
    border-top-right-radius: 0 !important
}

.rounded-top-1 {
    border-top-left-radius: var(--mdb-border-radius-sm) !important;
    border-top-right-radius: var(--mdb-border-radius-sm) !important
}

.rounded-top-2 {
    border-top-left-radius: var(--mdb-border-radius) !important;
    border-top-right-radius: var(--mdb-border-radius) !important
}

.rounded-top-3 {
    border-top-left-radius: var(--mdb-border-radius-lg) !important;
    border-top-right-radius: var(--mdb-border-radius-lg) !important
}

.rounded-top-4 {
    border-top-left-radius: var(--mdb-border-radius-xl) !important;
    border-top-right-radius: var(--mdb-border-radius-xl) !important
}

.rounded-top-5 {
    border-top-left-radius: var(--mdb-border-radius-xxl) !important;
    border-top-right-radius: var(--mdb-border-radius-xxl) !important
}

.rounded-top-circle {
    border-top-left-radius: 50% !important;
    border-top-right-radius: 50% !important
}

.rounded-top-pill {
    border-top-left-radius: var(--mdb-border-radius-pill) !important;
    border-top-right-radius: var(--mdb-border-radius-pill) !important
}

.rounded-end {
    border-top-right-radius: var(--mdb-border-radius) !important;
    border-bottom-right-radius: var(--mdb-border-radius) !important
}

.rounded-end-0 {
    border-top-right-radius: 0 !important;
    border-bottom-right-radius: 0 !important
}

.rounded-end-1 {
    border-top-right-radius: var(--mdb-border-radius-sm) !important;
    border-bottom-right-radius: var(--mdb-border-radius-sm) !important
}

.rounded-end-2 {
    border-top-right-radius: var(--mdb-border-radius) !important;
    border-bottom-right-radius: var(--mdb-border-radius) !important
}

.rounded-end-3 {
    border-top-right-radius: var(--mdb-border-radius-lg) !important;
    border-bottom-right-radius: var(--mdb-border-radius-lg) !important
}

.rounded-end-4 {
    border-top-right-radius: var(--mdb-border-radius-xl) !important;
    border-bottom-right-radius: var(--mdb-border-radius-xl) !important
}

.rounded-end-5 {
    border-top-right-radius: var(--mdb-border-radius-xxl) !important;
    border-bottom-right-radius: var(--mdb-border-radius-xxl) !important
}

.rounded-end-circle {
    border-top-right-radius: 50% !important;
    border-bottom-right-radius: 50% !important
}

.rounded-end-pill {
    border-top-right-radius: var(--mdb-border-radius-pill) !important;
    border-bottom-right-radius: var(--mdb-border-radius-pill) !important
}

.rounded-bottom {
    border-bottom-right-radius: var(--mdb-border-radius) !important;
    border-bottom-left-radius: var(--mdb-border-radius) !important
}

.rounded-bottom-0 {
    border-bottom-right-radius: 0 !important;
    border-bottom-left-radius: 0 !important
}

.rounded-bottom-1 {
    border-bottom-right-radius: var(--mdb-border-radius-sm) !important;
    border-bottom-left-radius: var(--mdb-border-radius-sm) !important
}

.rounded-bottom-2 {
    border-bottom-right-radius: var(--mdb-border-radius) !important;
    border-bottom-left-radius: var(--mdb-border-radius) !important
}

.rounded-bottom-3 {
    border-bottom-right-radius: var(--mdb-border-radius-lg) !important;
    border-bottom-left-radius: var(--mdb-border-radius-lg) !important
}

.rounded-bottom-4 {
    border-bottom-right-radius: var(--mdb-border-radius-xl) !important;
    border-bottom-left-radius: var(--mdb-border-radius-xl) !important
}

.rounded-bottom-5 {
    border-bottom-right-radius: var(--mdb-border-radius-xxl) !important;
    border-bottom-left-radius: var(--mdb-border-radius-xxl) !important
}

.rounded-bottom-circle {
    border-bottom-right-radius: 50% !important;
    border-bottom-left-radius: 50% !important
}

.rounded-bottom-pill {
    border-bottom-right-radius: var(--mdb-border-radius-pill) !important;
    border-bottom-left-radius: var(--mdb-border-radius-pill) !important
}

.rounded-start {
    border-bottom-left-radius: var(--mdb-border-radius) !important;
    border-top-left-radius: var(--mdb-border-radius) !important
}

.rounded-start-0 {
    border-bottom-left-radius: 0 !important;
    border-top-left-radius: 0 !important
}

.rounded-start-1 {
    border-bottom-left-radius: var(--mdb-border-radius-sm) !important;
    border-top-left-radius: var(--mdb-border-radius-sm) !important
}

.rounded-start-2 {
    border-bottom-left-radius: var(--mdb-border-radius) !important;
    border-top-left-radius: var(--mdb-border-radius) !important
}

.rounded-start-3 {
    border-bottom-left-radius: var(--mdb-border-radius-lg) !important;
    border-top-left-radius: var(--mdb-border-radius-lg) !important
}

.rounded-start-4 {
    border-bottom-left-radius: var(--mdb-border-radius-xl) !important;
    border-top-left-radius: var(--mdb-border-radius-xl) !important
}

.rounded-start-5 {
    border-bottom-left-radius: var(--mdb-border-radius-xxl) !important;
    border-top-left-radius: var(--mdb-border-radius-xxl) !important
}

.rounded-start-circle {
    border-bottom-left-radius: 50% !important;
    border-top-left-radius: 50% !important
}

.rounded-start-pill {
    border-bottom-left-radius: var(--mdb-border-radius-pill) !important;
    border-top-left-radius: var(--mdb-border-radius-pill) !important
}

.visible {
    visibility: visible !important
}

.invisible {
    visibility: hidden !important
}

.z-n1 {
    z-index: -1 !important
}

.z-0 {
    z-index: 0 !important
}

.z-1 {
    z-index: 1 !important
}

.z-2 {
    z-index: 2 !important
}

.z-3 {
    z-index: 3 !important
}

.ls-tighter {
    letter-spacing: -0.05em !important
}

.ls-tight {
    letter-spacing: -0.025em !important
}

.ls-normal {
    letter-spacing: 0em !important
}

.ls-wide {
    letter-spacing: .025em !important
}

.ls-wider {
    letter-spacing: .05em !important
}

.ls-widest {
    letter-spacing: .1em !important
}

.object-top {
    object-position: top !important
}

.object-center {
    object-position: center !important
}

.object-bottom {
    object-position: bottom !important
}


.diagonal-fractions {
    font-variant-numeric: diagonal-fractions
}

.bg-super-light {
    --mdb-bg-super-light: #fbfbfb;
    background-color: var(--mdb-bg-super-light)
}

.bg-fixed {
    background-attachment: fixed
}

.bg-local {
    background-attachment: local
}

.bg-scroll {
    background-attachment: scroll
}

.overflow-y-scroll {
    overflow-y: scroll
}

.overflow-x-scroll {
    overflow-x: scroll
}

.table-fixed {
    table-layout: fixed
}

.table-auto {
    table-layout: auto
}

.link-primary {
    transition: color .15s
}

.link-secondary {
    transition: color .15s
}

.link-success {
    transition: color .15s
}

.link-danger {
    transition: color .15s
}

.link-warning {
    transition: color .15s
}

.link-info {
    transition: color .15s
}

.link-light {
    transition: color .15s
}

.link-dark {
    transition: color .15s
}

:root,
[data-mdb-theme=light] {
    --mdb-font-roboto: "Roboto", sans-serif;
    --mdb-bg-opacity: 1;
    --mdb-text-hover-opacity: 0.8;
    --mdb-surface-color: #4f4f4f;
    --mdb-surface-color-rgb: 79, 79, 79;
    --mdb-surface-bg: #fff;
    --mdb-surface-inverted-color: #fff;
    --mdb-surface-inverted-color-rgb: 255, 255, 255;
    --mdb-surface-inverted-bg: #6d6d6d;
    --mdb-divider-color: #f5f5f5;
    --mdb-divider-blurry-color: hsl(0, 0%, 40%);
    --mdb-highlight-bg-color: #eeeeee;
    --mdb-scrollbar-rail-bg: #eeeeee;
    --mdb-scrollbar-thumb-bg: #9e9e9e;
    --mdb-picker-header-bg: #3b71ca;
    --mdb-timepicker-clock-face-bg: var(--mdb-secondary-bg);
    --mdb-sidenav-backdrop-opacity: 0.1;
    --mdb-form-control-border-color: #bdbdbd;
    --mdb-form-control-label-color: #757575;
    --mdb-form-control-disabled-bg: #e0e0e0;
    --mdb-box-shadow-color: #000;
    --mdb-box-shadow-color-rgb: 0, 0, 0;
    --mdb-stepper-mobile-bg: #fbfbfb
}

[data-mdb-theme=dark] {
    color-scheme: dark;
    --mdb-surface-color: #fff;
    --mdb-surface-color-rgb: 255, 255, 255;
    --mdb-surface-bg: #424242;
    --mdb-surface-inverted-color: #fff;
    --mdb-surface-inverted-color-rgb: 255, 255, 255;
    --mdb-surface-inverted-bg: #757575;
    --mdb-divider-color: rgba(255, 255, 255, 0.12);
    --mdb-divider-blurry-color: hsl(0, 0%, 70%);
    --mdb-highlight-bg-color: #3c3c3c;
    --mdb-scrollbar-rail-bg: #9e9e9e;
    --mdb-scrollbar-thumb-bg: #eeeeee;
    --mdb-picker-header-bg: #323232;
    --mdb-timepicker-clock-face-bg: #616161;
    --mdb-sidenav-backdrop-opacity: 0.5;
    --mdb-form-control-border-color: rgba(255, 255, 255, 0.7);
    --mdb-form-control-label-color: #bdbdbd;
    --mdb-form-control-disabled-bg: #616161;
    --mdb-box-shadow-color: #000;
    --mdb-box-shadow-color-rgb: 0, 0, 0;
    --mdb-stepper-mobile-bg: #3b3b3b
}

hr:not([size]).hr {
    --mdb-divider-height: 2px;
    --mdb-divider-bg: var(--mdb-divider-color);
    --mdb-divider-opacity: 1;
    --mdb-divider-blurry-bg: transparent;
    --mdb-divider-blurry-bg-image: linear-gradient(90deg, transparent, var(--mdb-divider-blurry-color), transparent);
    --mdb-divider-blurry-height: 1px;
    --mdb-divider-blurry-opacity: 0.25;
    height: var(--mdb-divider-height);
    background-color: var(--mdb-divider-bg);
    opacity: var(--mdb-divider-opacity)
}

hr:not([size]).hr.hr-blurry {
    background-color: var(--mdb-divider-blurry-bg);
    background-image: var(--mdb-divider-blurry-bg-image);
    height: var(--mdb-divider-blurry-height);
    opacity: var(--mdb-divider-blurry-opacity)
}

hr:not([size]).vr {
    height: auto
}

hr.hr,
hr.vr {
    border-top: none !important
}

.vr {
    --mdb-divider-width: 2px;
    --mdb-divider-bg: var(--mdb-divider-color);
    --mdb-divider-opacity: 1;
    width: var(--mdb-divider-width);
    background-color: var(--mdb-divider-bg);
    opacity: var(--mdb-divider-opacity)
}

.vr-blurry {
    --mdb-divider-blurry-vr-bg-image: linear-gradient(180deg, transparent, var(--mdb-divider-blurry-color), transparent);
    --mdb-divider-blurry-vr-width: 1px;
    --mdb-divider-blurry-opacity: 0.25;
    background-image: var(--mdb-divider-blurry-vr-bg-image);
    width: var(--mdb-divider-blurry-vr-width);
    opacity: var(--mdb-divider-blurry-opacity)
}

a {
    --mdb-link-decoration: none;
    text-decoration: var(--mdb-link-decoration)
}

.note {
    --mdb-note-padding: 10px;
    --mdb-note-border-width: 6px;
    --mdb-note-border-radius: 5px;
    --mdb-note-strong-font-weight: 600;
    padding: var(--mdb-note-padding);
    border-left: var(--mdb-note-border-width) solid;
    border-radius: var(--mdb-note-border-radius)
}

.note strong {
    font-weight: var(--mdb-note-strong-font-weight)
}

.note-primary {
    background-color: var(--mdb-primary-bg-subtle);
    color: var(--mdb-primary-text-emphasis)
}

.note-secondary {
    background-color: var(--mdb-secondary-bg-subtle);
    color: var(--mdb-secondary-text-emphasis)
}

.note-success {
    background-color: var(--mdb-success-bg-subtle);
    color: var(--mdb-success-text-emphasis)
}

.note-danger {
    background-color: var(--mdb-danger-bg-subtle);
    color: var(--mdb-danger-text-emphasis)
}

.note-warning {
    background-color: var(--mdb-warning-bg-subtle);
    color: var(--mdb-warning-text-emphasis)
}

.note-info {
    background-color: var(--mdb-info-bg-subtle);
    color: var(--mdb-info-text-emphasis)
}

.note-light {
    background-color: var(--mdb-light-bg-subtle);
    color: var(--mdb-light-text-emphasis)
}

.note-dark {
    background-color: var(--mdb-dark-bg-subtle);
    color: var(--mdb-dark-text-emphasis)
}

@media(min-width: 1199px) {
    .w-responsive {
        width: 75%
    }
}

.bg-primary {
    --mdb--bg-opacity: 1;
    background-color: rgba(59, 113, 202, var(--mdb--bg-opacity))
}

.bg-secondary {
    --mdb--bg-opacity: 1;
    background-color: rgba(159, 166, 178, var(--mdb--bg-opacity))
}

.bg-success {
    --mdb--bg-opacity: 1;
    background-color: rgba(20, 164, 77, var(--mdb--bg-opacity))
}

.bg-danger {
    --mdb--bg-opacity: 1;
    background-color: rgba(220, 76, 100, var(--mdb--bg-opacity))
}

.bg-warning {
    --mdb--bg-opacity: 1;
    background-color: rgba(228, 161, 27, var(--mdb--bg-opacity))
}

.bg-info {
    --mdb--bg-opacity: 1;
    background-color: rgba(84, 180, 211, var(--mdb--bg-opacity))
}

.bg-light {
    --mdb--bg-opacity: 1;
    background-color: rgba(251, 251, 251, var(--mdb--bg-opacity))
}

.bg-dark {
    --mdb--bg-opacity: 1;
    background-color: rgba(51, 45, 45, var(--mdb--bg-opacity))
}

/*!
 * # Semantic UI 2.4.2 - Flag
 * http://github.com/semantic-org/semantic-ui/
 *
 *
 * Released under the MIT license
 * http://opensource.org/licenses/MIT
 *
 */
#mdb-table-flag tr {
    cursor: pointer
}

.mdb-flag-selected {
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    text-align: center;
    max-width: 150px;
    margin: 0 auto;
    margin-top: 10px
}

.mdb-selected-flag-text {
    margin: 0 auto;
    max-width: 150px
}

i.flag:not(.icon) {
    display: inline-block;
    width: 16px;
    height: 11px;
    margin: 0 .5em 0 0;
    line-height: 11px;
    text-decoration: inherit;
    vertical-align: baseline;
    backface-visibility: hidden
}

i.flag::before {
    display: inline-block;
    width: 16px;
    height: 11px;
    content: "";
    background: url("https://mdbootstrap.com/img/svg/flags.png") no-repeat -108px -1976px
}

i.flag-ad:before,
i.flag-andorra:before {
    background-position: 0 0 !important
}

i.flag-ae:before,
i.flag-united-arab-emirates:before,
i.flag-uae:before {
    background-position: 0 -26px !important
}

i.flag-af:before,
i.flag-afghanistan:before {
    background-position: 0 -52px !important
}

i.flag-ag:before,
i.flag-antigua:before {
    background-position: 0 -78px !important
}

i.flag-ai:before,
i.flag-anguilla:before {
    background-position: 0 -104px !important
}

i.flag-al:before,
i.flag-albania:before {
    background-position: 0 -130px !important
}

i.flag-am:before,
i.flag-armenia:before {
    background-position: 0 -156px !important
}

i.flag-an:before,
i.flag-netherlands-antilles:before {
    background-position: 0 -182px !important
}

i.flag-ao:before,
i.flag-angola:before {
    background-position: 0 -208px !important
}

i.flag-ar:before,
i.flag-argentina:before {
    background-position: 0 -234px !important
}

i.flag-as:before,
i.flag-american-samoa:before {
    background-position: 0 -260px !important
}

i.flag-at:before,
i.flag-austria:before {
    background-position: 0 -286px !important
}

i.flag-au:before,
i.flag-australia:before {
    background-position: 0 -312px !important
}

i.flag-aw:before,
i.flag-aruba:before {
    background-position: 0 -338px !important
}

i.flag-ax:before,
i.flag-aland-islands:before {
    background-position: 0 -364px !important
}

i.flag-az:before,
i.flag-azerbaijan:before {
    background-position: 0 -390px !important
}

i.flag-ba:before,
i.flag-bosnia:before {
    background-position: 0 -416px !important
}

i.flag-bb:before,
i.flag-barbados:before {
    background-position: 0 -442px !important
}

i.flag-bd:before,
i.flag-bangladesh:before {
    background-position: 0 -468px !important
}

i.flag-be:before,
i.flag-belgium:before {
    background-position: 0 -494px !important
}

i.flag-bf:before,
i.flag-burkina-faso:before {
    background-position: 0 -520px !important
}

i.flag-bg:before,
i.flag-bulgaria:before {
    background-position: 0 -546px !important
}

i.flag-bh:before,
i.flag-bahrain:before {
    background-position: 0 -572px !important
}

i.flag-bi:before,
i.flag-burundi:before {
    background-position: 0 -598px !important
}

i.flag-bj:before,
i.flag-benin:before {
    background-position: 0 -624px !important
}

i.flag-bm:before,
i.flag-bermuda:before {
    background-position: 0 -650px !important
}

i.flag-bn:before,
i.flag-brunei:before {
    background-position: 0 -676px !important
}

i.flag-bo:before,
i.flag-bolivia:before {
    background-position: 0 -702px !important
}

i.flag-br:before,
i.flag-brazil:before {
    background-position: 0 -728px !important
}

i.flag-bs:before,
i.flag-bahamas:before {
    background-position: 0 -754px !important
}

i.flag-bt:before,
i.flag-bhutan:before {
    background-position: 0 -780px !important
}

i.flag-bv:before,
i.flag-bouvet-island:before {
    background-position: 0 -806px !important
}

i.flag-bw:before,
i.flag-botswana:before {
    background-position: 0 -832px !important
}

i.flag-by:before,
i.flag-belarus:before {
    background-position: 0 -858px !important
}

i.flag-bz:before,
i.flag-belize:before {
    background-position: 0 -884px !important
}

i.flag-ca:before,
i.flag-canada:before {
    background-position: 0 -910px !important
}

i.flag-cc:before,
i.flag-cocos-islands:before {
    background-position: 0 -962px !important
}

i.flag-cd:before,
i.flag-congo:before {
    background-position: 0 -988px !important
}

i.flag-cf:before,
i.flag-central-african-republic:before {
    background-position: 0 -1014px !important
}

i.flag-cg:before,
i.flag-congo-brazzaville:before {
    background-position: 0 -1040px !important
}

i.flag-ch:before,
i.flag-switzerland:before {
    background-position: 0 -1066px !important
}

i.flag-ci:before,
i.flag-cote-divoire:before {
    background-position: 0 -1092px !important
}

i.flag-ck:before,
i.flag-cook-islands:before {
    background-position: 0 -1118px !important
}

i.flag-cl:before,
i.flag-chile:before {
    background-position: 0 -1144px !important
}

i.flag-cm:before,
i.flag-cameroon:before {
    background-position: 0 -1170px !important
}

i.flag-cn:before,
i.flag-china:before {
    background-position: 0 -1196px !important
}

i.flag-co:before,
i.flag-colombia:before {
    background-position: 0 -1222px !important
}

i.flag-cr:before,
i.flag-costa-rica:before {
    background-position: 0 -1248px !important
}

i.flag-cs:before,
i.flag-serbia:before {
    background-position: 0 -1274px !important
}

i.flag-cu:before,
i.flag-cuba:before {
    background-position: 0 -1300px !important
}

i.flag-cv:before,
i.flag-cape-verde:before {
    background-position: 0 -1326px !important
}

i.flag-cx:before,
i.flag-christmas-island:before {
    background-position: 0 -1352px !important
}

i.flag-cy:before,
i.flag-cyprus:before {
    background-position: 0 -1378px !important
}

i.flag-cz:before,
i.flag-czech-republic:before {
    background-position: 0 -1404px !important
}

i.flag-de:before,
i.flag-germany:before {
    background-position: 0 -1430px !important
}

i.flag-dj:before,
i.flag-djibouti:before {
    background-position: 0 -1456px !important
}

i.flag-dk:before,
i.flag-denmark:before {
    background-position: 0 -1482px !important
}

i.flag-dm:before,
i.flag-dominica:before {
    background-position: 0 -1508px !important
}

i.flag-do:before,
i.flag-dominican-republic:before {
    background-position: 0 -1534px !important
}

i.flag-dz:before,
i.flag-algeria:before {
    background-position: 0 -1560px !important
}

i.flag-ec:before,
i.flag-ecuador:before {
    background-position: 0 -1586px !important
}

i.flag-ee:before,
i.flag-estonia:before {
    background-position: 0 -1612px !important
}

i.flag-eg:before,
i.flag-egypt:before {
    background-position: 0 -1638px !important
}

i.flag-eh:before,
i.flag-western-sahara:before {
    background-position: 0 -1664px !important
}

i.flag-gb-eng:before,
i.flag-england:before {
    background-position: 0 -1690px !important
}

i.flag-er:before,
i.flag-eritrea:before {
    background-position: 0 -1716px !important
}

i.flag-es:before,
i.flag-spain:before {
    background-position: 0 -1742px !important
}

i.flag-et:before,
i.flag-ethiopia:before {
    background-position: 0 -1768px !important
}

i.flag-eu:before,
i.flag-european-union:before {
    background-position: 0 -1794px !important
}

i.flag-fi:before,
i.flag-finland:before {
    background-position: 0 -1846px !important
}

i.flag-fj:before,
i.flag-fiji:before {
    background-position: 0 -1872px !important
}

i.flag-fk:before,
i.flag-falkland-islands:before {
    background-position: 0 -1898px !important
}

i.flag-fm:before,
i.flag-micronesia:before {
    background-position: 0 -1924px !important
}

i.flag-fo:before,
i.flag-faroe-islands:before {
    background-position: 0 -1950px !important
}

i.flag-fr:before,
i.flag-france:before {
    background-position: 0 -1976px !important
}

i.flag-ga:before,
i.flag-gabon:before {
    background-position: -36px 0 !important
}

i.flag-gb:before,
i.flag-uk:before,
i.flag-united-kingdom:before {
    background-position: -36px -26px !important
}

i.flag-gd:before,
i.flag-grenada:before {
    background-position: -36px -52px !important
}

i.flag-ge:before,
i.flag-georgia:before {
    background-position: -36px -78px !important
}

i.flag-gf:before,
i.flag-french-guiana:before {
    background-position: -36px -104px !important
}

i.flag-gh:before,
i.flag-ghana:before {
    background-position: -36px -130px !important
}

i.flag-gi:before,
i.flag-gibraltar:before {
    background-position: -36px -156px !important
}

i.flag-gl:before,
i.flag-greenland:before {
    background-position: -36px -182px !important
}

i.flag-gm:before,
i.flag-gambia:before {
    background-position: -36px -208px !important
}

i.flag-gn:before,
i.flag-guinea:before {
    background-position: -36px -234px !important
}

i.flag-gp:before,
i.flag-guadeloupe:before {
    background-position: -36px -260px !important
}

i.flag-gq:before,
i.flag-equatorial-guinea:before {
    background-position: -36px -286px !important
}

i.flag-gr:before,
i.flag-greece:before {
    background-position: -36px -312px !important
}

i.flag-gs:before,
i.flag-sandwich-islands:before {
    background-position: -36px -338px !important
}

i.flag-gt:before,
i.flag-guatemala:before {
    background-position: -36px -364px !important
}

i.flag-gu:before,
i.flag-guam:before {
    background-position: -36px -390px !important
}

i.flag-gw:before,
i.flag-guinea-bissau:before {
    background-position: -36px -416px !important
}

i.flag-gy:before,
i.flag-guyana:before {
    background-position: -36px -442px !important
}

i.flag-hk:before,
i.flag-hong-kong:before {
    background-position: -36px -468px !important
}

i.flag-hm:before,
i.flag-heard-island:before {
    background-position: -36px -494px !important
}

i.flag-hn:before,
i.flag-honduras:before {
    background-position: -36px -520px !important
}

i.flag-hr:before,
i.flag-croatia:before {
    background-position: -36px -546px !important
}

i.flag-ht:before,
i.flag-haiti:before {
    background-position: -36px -572px !important
}

i.flag-hu:before,
i.flag-hungary:before {
    background-position: -36px -598px !important
}

i.flag-id:before,
i.flag-indonesia:before {
    background-position: -36px -624px !important
}

i.flag-ie:before,
i.flag-ireland:before {
    background-position: -36px -650px !important
}

i.flag-il:before,
i.flag-israel:before {
    background-position: -36px -676px !important
}

i.flag-in:before,
i.flag-india:before {
    background-position: -36px -702px !important
}

i.flag-io:before,
i.flag-indian-ocean-territory:before {
    background-position: -36px -728px !important
}

i.flag-iq:before,
i.flag-iraq:before {
    background-position: -36px -754px !important
}

i.flag-ir:before,
i.flag-iran:before {
    background-position: -36px -780px !important
}

i.flag-is:before,
i.flag-iceland:before {
    background-position: -36px -806px !important
}

i.flag-it:before,
i.flag-italy:before {
    background-position: -36px -832px !important
}

i.flag-jm:before,
i.flag-jamaica:before {
    background-position: -36px -858px !important
}

i.flag-jo:before,
i.flag-jordan:before {
    background-position: -36px -884px !important
}

i.flag-jp:before,
i.flag-japan:before {
    background-position: -36px -910px !important
}

i.flag-ke:before,
i.flag-kenya:before {
    background-position: -36px -936px !important
}

i.flag-kg:before,
i.flag-kyrgyzstan:before {
    background-position: -36px -962px !important
}

i.flag-kh:before,
i.flag-cambodia:before {
    background-position: -36px -988px !important
}

i.flag-ki:before,
i.flag-kiribati:before {
    background-position: -36px -1014px !important
}

i.flag-km:before,
i.flag-comoros:before {
    background-position: -36px -1040px !important
}

i.flag-kn:before,
i.flag-saint-kitts-and-nevis:before {
    background-position: -36px -1066px !important
}

i.flag-kp:before,
i.flag-north-korea:before {
    background-position: -36px -1092px !important
}

i.flag-kr:before,
i.flag-south-korea:before {
    background-position: -36px -1118px !important
}

i.flag-kw:before,
i.flag-kuwait:before {
    background-position: -36px -1144px !important
}

i.flag-ky:before,
i.flag-cayman-islands:before {
    background-position: -36px -1170px !important
}

i.flag-kz:before,
i.flag-kazakhstan:before {
    background-position: -36px -1196px !important
}

i.flag-la:before,
i.flag-laos:before {
    background-position: -36px -1222px !important
}

i.flag-lb:before,
i.flag-lebanon:before {
    background-position: -36px -1248px !important
}

i.flag-lc:before,
i.flag-saint-lucia:before {
    background-position: -36px -1274px !important
}

i.flag-li:before,
i.flag-liechtenstein:before {
    background-position: -36px -1300px !important
}

i.flag-lk:before,
i.flag-sri-lanka:before {
    background-position: -36px -1326px !important
}

i.flag-lr:before,
i.flag-liberia:before {
    background-position: -36px -1352px !important
}

i.flag-ls:before,
i.flag-lesotho:before {
    background-position: -36px -1378px !important
}

i.flag-lt:before,
i.flag-lithuania:before {
    background-position: -36px -1404px !important
}

i.flag-lu:before,
i.flag-luxembourg:before {
    background-position: -36px -1430px !important
}

i.flag-lv:before,
i.flag-latvia:before {
    background-position: -36px -1456px !important
}

i.flag-ly:before,
i.flag-libya:before {
    background-position: -36px -1482px !important
}

i.flag-ma:before,
i.flag-morocco:before {
    background-position: -36px -1508px !important
}

i.flag-mc:before,
i.flag-monaco:before {
    background-position: -36px -1534px !important
}

i.flag-md:before,
i.flag-moldova:before {
    background-position: -36px -1560px !important
}

i.flag-me:before,
i.flag-montenegro:before {
    background-position: -36px -1586px !important
}

i.flag-mg:before,
i.flag-madagascar:before {
    background-position: -36px -1613px !important
}

i.flag-mh:before,
i.flag-marshall-islands:before {
    background-position: -36px -1639px !important
}

i.flag-mk:before,
i.flag-macedonia:before {
    background-position: -36px -1665px !important
}

i.flag-ml:before,
i.flag-mali:before {
    background-position: -36px -1691px !important
}

i.flag-mm:before,
i.flag-myanmar:before,
i.flag-burma:before {
    background-position: -73px -1821px !important
}

i.flag-mn:before,
i.flag-mongolia:before {
    background-position: -36px -1743px !important
}

i.flag-mo:before,
i.flag-macau:before {
    background-position: -36px -1769px !important
}

i.flag-mp:before,
i.flag-northern-mariana-islands:before {
    background-position: -36px -1795px !important
}

i.flag-mq:before,
i.flag-martinique:before {
    background-position: -36px -1821px !important
}

i.flag-mr:before,
i.flag-mauritania:before {
    background-position: -36px -1847px !important
}

i.flag-ms:before,
i.flag-montserrat:before {
    background-position: -36px -1873px !important
}

i.flag-mt:before,
i.flag-malta:before {
    background-position: -36px -1899px !important
}

i.flag-mu:before,
i.flag-mauritius:before {
    background-position: -36px -1925px !important
}

i.flag-mv:before,
i.flag-maldives:before {
    background-position: -36px -1951px !important
}

i.flag-mw:before,
i.flag-malawi:before {
    background-position: -36px -1977px !important
}

i.flag-mx:before,
i.flag-mexico:before {
    background-position: -72px 0 !important
}

i.flag-my:before,
i.flag-malaysia:before {
    background-position: -72px -26px !important
}

i.flag-mz:before,
i.flag-mozambique:before {
    background-position: -72px -52px !important
}

i.flag-na:before,
i.flag-namibia:before {
    background-position: -72px -78px !important
}

i.flag-nc:before,
i.flag-new-caledonia:before {
    background-position: -72px -104px !important
}

i.flag-ne:before,
i.flag-niger:before {
    background-position: -72px -130px !important
}

i.flag-nf:before,
i.flag-norfolk-island:before {
    background-position: -72px -156px !important
}

i.flag-ng:before,
i.flag-nigeria:before {
    background-position: -72px -182px !important
}

i.flag-ni:before,
i.flag-nicaragua:before {
    background-position: -72px -208px !important
}

i.flag-nl:before,
i.flag-netherlands:before {
    background-position: -72px -234px !important
}

i.flag-no:before,
i.flag-norway:before {
    background-position: -72px -260px !important
}

i.flag-np:before,
i.flag-nepal:before {
    background-position: -72px -286px !important
}

i.flag-nr:before,
i.flag-nauru:before {
    background-position: -72px -312px !important
}

i.flag-nu:before,
i.flag-niue:before {
    background-position: -72px -338px !important
}

i.flag-nz:before,
i.flag-new-zealand:before {
    background-position: -72px -364px !important
}

i.flag-om:before,
i.flag-oman:before {
    background-position: -72px -390px !important
}

i.flag-pa:before,
i.flag-panama:before {
    background-position: -72px -416px !important
}

i.flag-pe:before,
i.flag-peru:before {
    background-position: -72px -442px !important
}

i.flag-pf:before,
i.flag-french-polynesia:before {
    background-position: -72px -468px !important
}

i.flag-pg:before,
i.flag-new-guinea:before {
    background-position: -72px -494px !important
}

i.flag-ph:before,
i.flag-philippines:before {
    background-position: -72px -520px !important
}

i.flag-pk:before,
i.flag-pakistan:before {
    background-position: -72px -546px !important
}

i.flag-pl:before,
i.flag-poland:before {
    background-position: -72px -572px !important
}

i.flag-pm:before,
i.flag-saint-pierre:before {
    background-position: -72px -598px !important
}

i.flag-pn:before,
i.flag-pitcairn-islands:before {
    background-position: -72px -624px !important
}

i.flag-pr:before,
i.flag-puerto-rico:before {
    background-position: -72px -650px !important
}

i.flag-ps:before,
i.flag-palestine:before {
    background-position: -72px -676px !important
}

i.flag-pt:before,
i.flag-portugal:before {
    background-position: -72px -702px !important
}

i.flag-pw:before,
i.flag-palau:before {
    background-position: -72px -728px !important
}

i.flag-py:before,
i.flag-paraguay:before {
    background-position: -72px -754px !important
}

i.flag-qa:before,
i.flag-qatar:before {
    background-position: -72px -780px !important
}

i.flag-re:before,
i.flag-reunion:before {
    background-position: -72px -806px !important
}

i.flag-ro:before,
i.flag-romania:before {
    background-position: -72px -832px !important
}

i.flag-rs:before,
i.flag-serbia:before {
    background-position: -72px -858px !important
}

i.flag-ru:before,
i.flag-russia:before {
    background-position: -72px -884px !important
}

i.flag-rw:before,
i.flag-rwanda:before {
    background-position: -72px -910px !important
}

i.flag-sa:before,
i.flag-saudi-arabia:before {
    background-position: -72px -936px !important
}

i.flag-sb:before,
i.flag-solomon-islands:before {
    background-position: -72px -962px !important
}

i.flag-sc:before,
i.flag-seychelles:before {
    background-position: -72px -988px !important
}

i.flag-gb-sct:before,
i.flag-scotland:before {
    background-position: -72px -1014px !important
}

i.flag-sd:before,
i.flag-sudan:before {
    background-position: -72px -1040px !important
}

i.flag-se:before,
i.flag-sweden:before {
    background-position: -72px -1066px !important
}

i.flag-sg:before,
i.flag-singapore:before {
    background-position: -72px -1092px !important
}

i.flag-sh:before,
i.flag-saint-helena:before {
    background-position: -72px -1118px !important
}

i.flag-si:before,
i.flag-slovenia:before {
    background-position: -72px -1144px !important
}

i.flag-sj:before,
i.flag-svalbard:before,
i.flag-jan-mayen:before {
    background-position: -72px -1170px !important
}

i.flag-sk:before,
i.flag-slovakia:before {
    background-position: -72px -1196px !important
}

i.flag-sl:before,
i.flag-sierra-leone:before {
    background-position: -72px -1222px !important
}

i.flag-sm:before,
i.flag-san-marino:before {
    background-position: -72px -1248px !important
}

i.flag-sn:before,
i.flag-senegal:before {
    background-position: -72px -1274px !important
}

i.flag-so:before,
i.flag-somalia:before {
    background-position: -72px -1300px !important
}

i.flag-sr:before,
i.flag-suriname:before {
    background-position: -72px -1326px !important
}

i.flag-st:before,
i.flag-sao-tome:before {
    background-position: -72px -1352px !important
}

i.flag-sv:before,
i.flag-el-salvador:before {
    background-position: -72px -1378px !important
}

i.flag-sy:before,
i.flag-syria:before {
    background-position: -72px -1404px !important
}

i.flag-sz:before,
i.flag-swaziland:before {
    background-position: -72px -1430px !important
}

i.flag-tc:before,
i.flag-caicos-islands:before {
    background-position: -72px -1456px !important
}

i.flag-td:before,
i.flag-chad:before {
    background-position: -72px -1482px !important
}

i.flag-tf:before,
i.flag-french-territories:before {
    background-position: -72px -1508px !important
}

i.flag-tg:before,
i.flag-togo:before {
    background-position: -72px -1534px !important
}

i.flag-th:before,
i.flag-thailand:before {
    background-position: -72px -1560px !important
}

i.flag-tj:before,
i.flag-tajikistan:before {
    background-position: -72px -1586px !important
}

i.flag-tk:before,
i.flag-tokelau:before {
    background-position: -72px -1612px !important
}

i.flag-tl:before,
i.flag-timorleste:before {
    background-position: -72px -1638px !important
}

i.flag-tm:before,
i.flag-turkmenistan:before {
    background-position: -72px -1664px !important
}

i.flag-tn:before,
i.flag-tunisia:before {
    background-position: -72px -1690px !important
}

i.flag-to:before,
i.flag-tonga:before {
    background-position: -72px -1716px !important
}

i.flag-tr:before,
i.flag-turkey:before {
    background-position: -72px -1742px !important
}

i.flag-tt:before,
i.flag-trinidad:before {
    background-position: -72px -1768px !important
}

i.flag-tv:before,
i.flag-tuvalu:before {
    background-position: -72px -1794px !important
}

i.flag-tw:before,
i.flag-taiwan:before {
    background-position: -72px -1820px !important
}

i.flag-tz:before,
i.flag-tanzania:before {
    background-position: -72px -1846px !important
}

i.flag-ua:before,
i.flag-ukraine:before {
    background-position: -72px -1872px !important
}

i.flag-ug:before,
i.flag-uganda:before {
    background-position: -72px -1898px !important
}

i.flag-um:before,
i.flag-us-minor-islands:before {
    background-position: -72px -1924px !important
}

i.flag-us:before,
i.flag-america:before,
i.flag-united-states:before {
    background-position: -72px -1950px !important
}

i.flag-uy:before,
i.flag-uruguay:before {
    background-position: -72px -1976px !important
}

i.flag-uz:before,
i.flag-uzbekistan:before {
    background-position: -108px 0 !important
}

i.flag-va:before,
i.flag-vatican-city:before {
    background-position: -108px -26px !important
}

i.flag-vc:before,
i.flag-saint-vincent:before {
    background-position: -108px -52px !important
}

i.flag-ve:before,
i.flag-venezuela:before {
    background-position: -108px -78px !important
}

i.flag-vg:before,
i.flag-british-virgin-islands:before {
    background-position: -108px -104px !important
}

i.flag-vi:before,
i.flag-us-virgin-islands:before {
    background-position: -108px -130px !important
}

i.flag-vn:before,
i.flag-vietnam:before {
    background-position: -108px -156px !important
}

i.flag-vu:before,
i.flag-vanuatu:before {
    background-position: -108px -182px !important
}

i.flag-gb-wls:before,
i.flag-wales:before {
    background-position: -108px -208px !important
}

i.flag-wf:before,
i.flag-wallis-and-futuna:before {
    background-position: -108px -234px !important
}

i.flag-ws:before,
i.flag-samoa:before {
    background-position: -108px -260px !important
}

i.flag-ye:before,
i.flag-yemen:before {
    background-position: -108px -286px !important
}

i.flag-yt:before,
i.flag-mayotte:before {
    background-position: -108px -312px !important
}

i.flag-za:before,
i.flag-south-africa:before {
    background-position: -108px -338px !important
}

i.flag-zm:before,
i.flag-zambia:before {
    background-position: -108px -364px !important
}

i.flag-zw:before,
i.flag-zimbabwe:before {
    background-position: -108px -390px !important
}

.bg-fixed {
    background-attachment: fixed
}

.bg-image {
    position: relative;
    overflow: hidden;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center center
}

.mask {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    background-attachment: fixed
}

.hover-overlay .mask {
    --mdb-image-hover-transition: all 0.3s ease-in-out;
    opacity: 0;
    transition: var(--mdb-image-hover-transition)
}

.hover-overlay .mask:hover {
    opacity: 1
}

.hover-zoom {
    --mdb-image-hover-zoom-transition: all 0.3s linear;
    --mdb-image-hover-zoom-transform: scale(1.1)
}

.hover-zoom img,
.hover-zoom video {
    transition: var(--mdb-image-hover-zoom-transition)
}

.hover-zoom:hover img,
.hover-zoom:hover video {
    transform: var(--mdb-image-hover-zoom-transform)
}

.hover-shadow,
.card.hover-shadow,
.hover-shadow-soft,
.card.hover-shadow-soft {
    --mdb-image-hover-shadow-transition: all 0.3s ease-in-out;
    transition: var(--mdb-image-hover-shadow-transition)
}

.hover-shadow:hover,
.card.hover-shadow:hover,
.hover-shadow-soft:hover,
.card.hover-shadow-soft:hover {
    transition: var(--mdb-image-hover-shadow-transition)
}

.hover-shadow,
.card.hover-shadow {
    --mdb-image-hover-shadow-box-shadow: 0 2px 15px -3px rgba(var(--mdb-box-shadow-color-rgb), 0.16), 0 10px 20px -2px rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    box-shadow: none
}

.hover-shadow:hover,
.card.hover-shadow:hover {
    box-shadow: var(--mdb-image-hover-shadow-box-shadow)
}

.hover-shadow-soft,
.card.hover-shadow-soft {
    --mdb-image-hover-shadow-box-shadow-soft: 0 2px 25px -5px rgba(var(--mdb-box-shadow-color-rgb), 0.07), 0 25px 21px -5px rgba(var(--mdb-box-shadow-color-rgb), 0.04);
    box-shadow: none
}

.hover-shadow-soft:hover,
.card.hover-shadow-soft:hover {
    box-shadow: var(--mdb-image-hover-shadow-box-shadow-soft)
}

.form-control {
    min-height: auto;
    padding: 4.5px 12px 3.68px 12px;
    transition: all .1s linear;
    box-shadow: none
}

.form-control:focus {
    box-shadow: none;
    transition: all .1s linear;
    border-color: #3b71ca;
    box-shadow: inset 0px 0px 0px 1px #3b71ca
}

.form-control.form-control-sm {
    font-size: .775rem;
    line-height: 1.5
}

.form-control.form-control-lg {
    line-height: 2.15;
    border-radius: .25rem
}

.form-outline {
    position: relative;
    width: 100%
}

.form-outline .form-helper {
    width: 100%;
    position: absolute;
    font-size: .875em;
    color: #757575
}

.form-outline .form-helper .form-counter {
    text-align: right
}

.form-outline .trailing {
    position: absolute;
    right: 10px;
    left: initial;
    top: 50%;
    transform: translateY(-50%);
    pointer-events: none;
    color: var(--mdb-surface-color)
}

.form-outline .form-icon-trailing {
    padding-right: 2rem !important
}

.form-outline .form-control {
    min-height: auto;
    padding-top: .32rem;
    padding-bottom: .32rem;
    padding-left: .75rem;
    padding-right: .75rem;
    border: 0;
    background: rgba(0, 0, 0, 0);
    transition: all .2s linear
}

.form-outline .form-control~.form-label {
    position: absolute;
    top: 0;
    max-width: 90%;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    left: .75rem;
    padding-top: .37rem;
    pointer-events: none;
    transform-origin: 0 0;
    transition: all .2s ease-out;
    color: var(--mdb-form-control-label-color);
    margin-bottom: 0
}

.form-outline .form-control~.form-notch {
    display: flex;
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    max-width: 100%;
    height: 100%;
    text-align: left;
    pointer-events: none
}

.form-outline .form-control~.form-notch div {
    pointer-events: none;
    border: 1px solid;
    border-color: var(--mdb-form-control-border-color);
    box-sizing: border-box;
    background: rgba(0, 0, 0, 0);
    transition: all .2s linear
}

.form-outline .form-control~.form-notch .form-notch-leading {
    left: 0;
    top: 0;
    height: 100%;
    width: .5rem;
    border-right: none;
    border-radius: .25rem 0 0 .25rem
}

.form-outline .form-control~.form-notch .form-notch-middle {
    flex: 0 0 auto;
    width: auto;
    max-width: calc(100% - 1rem);
    height: 100%;
    border-right: none;
    border-left: none
}

.form-outline .form-control~.form-notch .form-notch-trailing {
    flex-grow: 1;
    height: 100%;
    border-left: none;
    border-radius: 0 .25rem .25rem 0
}

.form-outline .form-control:not(.placeholder-active)::placeholder {
    opacity: 0
}

.form-outline .form-control:focus::placeholder,
.form-outline .form-control.active::placeholder {
    opacity: 1
}

.form-outline .form-control:focus {
    box-shadow: none !important
}

.form-outline .form-control:focus~.form-label,
.form-outline .form-control.active~.form-label {
    transform: translateY(-1rem) translateY(0.1rem) scale(0.8)
}

.form-outline .form-control:focus~.form-label {
    color: #3b71ca
}

.form-outline .form-control:focus~.form-notch .form-notch-middle,
.form-outline .form-control.active~.form-notch .form-notch-middle {
    border-right: none;
    border-left: none;
    border-top: 1px solid rgba(0, 0, 0, 0)
}

.form-outline .form-control:focus~.form-notch .form-notch-middle {
    border-color: #3b71ca;
    box-shadow: 0 1px 0 0 #3b71ca;
    border-top: 1px solid rgba(0, 0, 0, 0)
}

.form-outline .form-control:focus~.form-notch .form-notch-leading,
.form-outline .form-control.active~.form-notch .form-notch-leading {
    border-right: none
}

.form-outline .form-control:focus~.form-notch .form-notch-leading {
    border-color: #3b71ca;
    box-shadow: -1px 0 0 0 #3b71ca, 0 1px 0 0 #3b71ca, 0 -1px 0 0 #3b71ca
}

.form-outline .form-control:focus~.form-notch .form-notch-trailing,
.form-outline .form-control.active~.form-notch .form-notch-trailing {
    border-left: none
}

.form-outline .form-control:focus~.form-notch .form-notch-trailing {
    border-color: #3b71ca;
    box-shadow: 1px 0 0 0 #3b71ca, 0 -1px 0 0 #3b71ca, 0 1px 0 0 #3b71ca
}

.form-outline .form-control:disabled,
.form-outline .form-control.disabled,
.form-outline .form-control[readonly] {
    background-color: var(--mdb-form-control-disabled-bg)
}

.form-outline .form-control:disabled~.timepicker-toggle-button,
.form-outline .form-control:disabled~.datepicker-toggle-button,
.form-outline .form-control:disabled~.datetimepicker-toggle-button,
.form-outline .form-control:disabled~.select-arrow,
.form-outline .form-control:disabled~.trailing,
.form-outline .form-control.disabled~.timepicker-toggle-button,
.form-outline .form-control.disabled~.datepicker-toggle-button,
.form-outline .form-control.disabled~.datetimepicker-toggle-button,
.form-outline .form-control.disabled~.select-arrow,
.form-outline .form-control.disabled~.trailing,
.form-outline .form-control[readonly]~.timepicker-toggle-button,
.form-outline .form-control[readonly]~.datepicker-toggle-button,
.form-outline .form-control[readonly]~.datetimepicker-toggle-button,
.form-outline .form-control[readonly]~.select-arrow,
.form-outline .form-control[readonly]~.trailing {
    color: rgba(var(--mdb-surface-color-rgb), 0.5)
}

.form-outline .form-control.form-control-lg {
    font-size: 1rem;
    line-height: 2.15
}

.form-outline .form-control.form-control-lg~.form-label {
    padding-top: .7rem
}

.form-outline .form-control.form-control-lg:focus~.form-label,
.form-outline .form-control.form-control-lg.active~.form-label {
    transform: translateY(-1.25rem) translateY(0.1rem) scale(0.8)
}

.form-outline .form-control.form-control-sm {
    padding-top: .32rem;
    padding-bottom: .32rem;
    font-size: .775rem;
    line-height: 1.5
}

.form-outline .form-control.form-control-sm~.form-label {
    padding-top: .33rem;
    font-size: .775rem
}

.form-outline .form-control.form-control-sm:focus~.form-label,
.form-outline .form-control.form-control-sm.active~.form-label {
    transform: translateY(-0.85rem) translateY(0.1rem) scale(0.8)
}

.form-outline.form-white .form-control {
    color: #fff
}

.form-outline.form-white .form-control~.form-label {
    color: #fbfbfb
}

.form-outline.form-white .form-control~.form-notch div {
    border-color: #fbfbfb
}

.form-outline.form-white .form-control:focus~.form-label {
    color: #fff
}

.form-outline.form-white .form-control:focus~.form-notch .form-notch-middle {
    border-color: #fff;
    box-shadow: 0 1px 0 0 #fff;
    border-top: 1px solid rgba(0, 0, 0, 0)
}

.form-outline.form-white .form-control:focus~.form-notch .form-notch-leading {
    border-color: #fff;
    box-shadow: -1px 0 0 0 #fff, 0 1px 0 0 #fff, 0 -1px 0 0 #fff
}

.form-outline.form-white .form-control:focus~.form-notch .form-notch-trailing {
    border-color: #fff;
    box-shadow: 1px 0 0 0 #fff, 0 -1px 0 0 #fff, 0 1px 0 0 #fff
}

.form-outline.form-white .form-control::placeholder {
    color: rgba(255, 255, 255, .7)
}

.form-outline.form-white .form-control:disabled,
.form-outline.form-white .form-control.disabled,
.form-outline.form-white .form-control[readonly] {
    background-color: rgba(255, 255, 255, .45)
}

.select-input.form-control[readonly]:not([disabled]) {
    background-color: rgba(0, 0, 0, 0)
}

.form-select {
    transition: all .2s linear
}

.form-select:focus {
    border-color: #3b71ca;
    outline: 0;
    box-shadow: inset 0px 0px 0px 1px #3b71ca
}

.form-check {
    min-height: 1.5rem
}

.form-check-input {
    position: relative;
    width: 1.125rem;
    height: 1.125rem;
    background-color: var(--mdb-body-bg);
    border: .125rem solid var(--mdb-form-control-border-color)
}

.form-check-input:before {
    content: "";
    position: absolute;
    box-shadow: 0px 0px 0px 13px rgba(0, 0, 0, 0);
    border-radius: 50%;
    width: .875rem;
    height: .875rem;
    background-color: rgba(0, 0, 0, 0);
    opacity: 0;
    pointer-events: none;
    transform: scale(0)
}

.form-check-input:hover {
    cursor: pointer
}

.form-check-input:hover:before {
    opacity: .04;
    box-shadow: 0px 0px 0px 13px rgba(var(--mdb-box-shadow-color-rgb), 0.6)
}

.form-check-input:focus {
    box-shadow: none;
    border-color: var(--mdb-form-control-border-color);
    transition: border-color .2s
}

.form-check-input:focus:before {
    opacity: .12;
    box-shadow: 0px 0px 0px 13px rgba(var(--mdb-box-shadow-color-rgb), 0.6);
    transform: scale(1);
    transition: box-shadow .2s, transform .2s
}

.form-check-input:checked {
    border-color: #3b71ca
}

.form-check-input:checked:before {
    opacity: .16
}

.form-check-input:checked:after {
    content: "";
    position: absolute
}

.form-check-input:checked:focus {
    border-color: #3b71ca
}

.form-check-input:checked:focus:before {
    box-shadow: 0px 0px 0px 13px #3b71ca;
    transform: scale(1);
    transition: box-shadow .2s, transform .2s
}

.form-check-input:indeterminate:focus:before {
    box-shadow: 0px 0px 0px 13px #3b71ca
}

.form-check-input[type=checkbox] {
    border-radius: .25rem;
    margin-top: .19em;
    margin-right: 6px
}

.form-check-input[type=checkbox]:focus:after {
    content: "";
    position: absolute;
    width: .875rem;
    height: .875rem;
    z-index: 1;
    display: block;
    border-radius: 0;
    background-color: var(--mdb-body-bg)
}

.form-check-input[type=checkbox]:checked {
    background-image: none;
    background-color: #3b71ca
}

.form-check-input[type=checkbox]:checked:after {
    display: block;
    transform: rotate(45deg)
        /*!rtl:ignore*/
    ;
    border-width: .125rem;
    border-color: #fff;
    width: .375rem;
    height: .8125rem;
    border-style: solid;
    border-top: 0;
    border-left: 0
        /*!rtl:ignore*/
    ;
    margin-left: .25rem;
    margin-top: -1px;
    background-color: rgba(0, 0, 0, 0)
}

.form-check-input[type=checkbox]:checked:focus {
    background-color: #3b71ca
}

.form-check-input[type=checkbox]:indeterminate {
    border-color: #3b71ca
}

.form-check-input[type=radio] {
    border-radius: 50%;
    width: 1.25rem;
    height: 1.25rem;
    margin-top: .125em;
    margin-right: 4px
}

.form-check-input[type=radio]:before {
    width: 1rem;
    height: 1rem
}

.form-check-input[type=radio]:after {
    content: "";
    position: absolute;
    width: 1rem;
    height: 1rem;
    z-index: 1;
    display: block;
    border-radius: 50%;
    background-color: var(--mdb-body-bg)
}

.form-check-input[type=radio]:checked {
    background-image: none;
    background-color: var(--mdb-body-bg)
}

.form-check-input[type=radio]:checked:after {
    border-radius: 50%;
    width: .625rem;
    height: .625rem;
    border-color: #3b71ca;
    background-color: #3b71ca;
    transition: border-color;
    transform: translate(-50%, -50%);
    position: absolute;
    left: 50%;
    top: 50%
}

.form-check-input[type=radio]:checked:focus {
    background-color: var(--mdb-body-bg)
}

.form-check-label {
    padding-left: .15rem
}

.form-check-label:hover {
    cursor: pointer
}

.form-switch .form-check-input {
    background-image: none;
    border-width: 0;
    border-radius: .4375rem;
    width: 2rem;
    height: .875rem;
    background-color: rgba(var(--mdb-emphasis-color-rgb), 0.25);
    margin-top: .3em;
    margin-right: 8px
}

.form-switch .form-check-input:after {
    content: "";
    position: absolute;
    border: none;
    z-index: 2;
    border-radius: 50%;
    width: 1.25rem;
    height: 1.25rem;
    background-color: var(--mdb-surface-bg);
    margin-top: -0.1875rem;
    box-shadow: 0 0px 3px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.07), 0 2px 2px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.04);
    transition: background-color .2s, transform .2s
}

.form-switch .form-check-input:focus {
    background-image: none
}

.form-switch .form-check-input:focus:before {
    box-shadow: 3px -1px 0px 13px rgba(var(--mdb-box-shadow-color-rgb), 0.6);
    transform: scale(1);
    transition: box-shadow .2s, transform .2s
}

.form-switch .form-check-input:focus:after {
    border-radius: 50%;
    width: 1.25rem;
    height: 1.25rem
}

.form-switch .form-check-input:checked {
    background-image: none
}

.form-switch .form-check-input:checked:focus {
    background-image: none
}

.form-switch .form-check-input:checked:focus:before {
    margin-left: 1.0625rem;
    box-shadow: 3px -1px 0px 13px #3b71ca;
    transform: scale(1);
    transition: box-shadow .2s, transform .2s
}

.form-switch .form-check-input:checked[type=checkbox] {
    background-image: none
}

.form-switch .form-check-input:checked[type=checkbox]:after {
    content: "";
    position: absolute;
    border: none;
    z-index: 2;
    border-radius: 50%;
    width: 1.25rem;
    height: 1.25rem;
    background-color: #3b71ca;
    margin-top: -3px;
    margin-left: 1.0625rem;
    box-shadow: 0 3px 1px -2px rgba(var(--mdb-box-shadow-color-rgb), 0.2), 0 2px 2px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.14), 0 1px 5px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.12);
    transition: background-color .2s, transform .2s
}

.form-control[type=file] {
    border-color: var(--mdb-form-control-border-color)
}

.form-control[type=file]::-webkit-file-upload-button {
    background-color: rgba(0, 0, 0, 0)
}

.form-control[type=file]:disabled {
    background-color: var(--mdb-form-control-disabled-bg);
    color: rgba(var(--mdb-surface-color-rgb), 0.5)
}

.form-control[type=file]:disabled::file-selector-button {
    color: rgba(var(--mdb-surface-color-rgb), 0.5)
}

.form-control:hover:not(:disabled):not([readonly])::-webkit-file-upload-button {
    background-color: rgba(0, 0, 0, 0)
}

.input-group {
    flex-wrap: nowrap
}

.input-group>.form-control {
    min-height: calc(2.08rem + 2px);
    height: calc(2.08rem + 2px);
    padding-top: .27rem;
    padding-bottom: .27rem;
    transition: all .2s linear
}

.input-group>.form-control:focus {
    transition: all .2s linear;
    border-color: #3b71ca;
    outline: 0;
    box-shadow: inset 0 0 0 1px #3b71ca
}

.input-group-text {
    background-color: rgba(0, 0, 0, 0);
    padding-top: .26rem;
    padding-bottom: .26rem
}

.input-group-text>.form-check-input[type=checkbox] {
    margin-left: 1px;
    margin-right: 1px
}

.input-group-text>.form-check-input[type=radio] {
    margin-right: 0
}

.input-group-lg>.form-control {
    height: calc(2.645rem + 2px);
    font-size: 1rem;
    padding-top: .33rem;
    padding-bottom: .33rem
}

.input-group-lg .input-group-text {
    font-size: 1rem
}

.input-group-sm>.form-control {
    min-height: calc(1.66rem + 2px);
    height: calc(1.66rem + 2px);
    font-size: .775rem;
    padding-top: .33rem;
    padding-bottom: .33rem
}

.input-group-sm .input-group-text {
    font-size: .775rem;
    line-height: 1.5
}

.input-group.form-outline .input-group-text {
    border-left: 0
}

.input-group.form-outline input+.input-group-text {
    border: 0;
    border-left: 1px solid #bdbdbd
}

.input-group .form-outline:not(:first-child),
.input-group .select-wrapper:not(:first-child),
.input-group .form-outline:not(:first-child) .form-notch-leading,
.input-group .select-wrapper:not(:first-child) .form-notch-leading {
    border-top-left-radius: 0 !important;
    border-bottom-left-radius: 0 !important
}

.input-group .form-outline:not(:last-child),
.input-group .select-wrapper:not(:last-child),
.input-group .form-outline:not(:last-child) .form-notch-trailing,
.input-group .select-wrapper:not(:last-child) .form-notch-trailing {
    border-top-right-radius: 0 !important;
    border-bottom-right-radius: 0 !important
}

.input-group>[class*=btn-outline-]+[class*=btn-outline-] {
    border-left: 0
}

.input-group>.btn[class*=btn-outline-] {
    padding-top: .47rem
}

.input-group>.btn {
    padding-top: .59rem
}

.input-group.input-group-lg .input-group-text {
    height: calc(2.645rem + 2px)
}

.input-group .input-group-text {
    height: calc(2.08rem + 2px)
}

.input-group .btn {
    line-height: 1
}

.input-group.input-group-sm .input-group-text {
    height: calc(1.66rem + 2px)
}

.was-validated .input-group .invalid-feedback,
.was-validated .input-group .valid-feedback {
    margin-top: 2.5rem
}

.input-group .invalid-feedback,
.input-group .valid-feedback {
    margin-top: 2.5rem
}

.valid-feedback {
    position: absolute;
    display: none;
    width: auto;
    margin-top: .25rem;
    font-size: .875rem;
    color: #14a44d;
    margin-top: -0.75rem
}

.valid-tooltip {
    position: absolute;
    top: 100%;
    z-index: 5;
    display: none;
    max-width: 100%;
    padding: 6px 16px;
    margin-top: .1rem;
    font-size: .875rem;
    background-color: rgba(20, 164, 77, .9);
    border-radius: .25rem !important;
    color: #fff
}

.was-validated :valid~.valid-feedback,
.was-validated :valid~.valid-tooltip,
.is-valid~.valid-feedback,
.is-valid~.valid-tooltip {
    display: block
}

.was-validated .form-control:valid,
.form-control.is-valid {
    margin-bottom: 1rem;
    background-image: none;
    border-color: #14a44d
}

.was-validated .form-control:valid:focus,
.form-control.is-valid:focus {
    border-color: #14a44d;
    box-shadow: 0 0 0 .25rem rgba(20, 164, 77, .25)
}

.was-validated .form-outline .form-control:valid~.form-label,
.form-outline .form-control.is-valid~.form-label {
    color: #14a44d
}

.was-validated .form-outline .form-control:valid~.form-notch .form-notch-leading,
.was-validated .form-outline .form-control:valid~.form-notch .form-notch-middle,
.was-validated .form-outline .form-control:valid~.form-notch .form-notch-trailing,
.form-outline .form-control.is-valid~.form-notch .form-notch-leading,
.form-outline .form-control.is-valid~.form-notch .form-notch-middle,
.form-outline .form-control.is-valid~.form-notch .form-notch-trailing {
    border-color: #14a44d
}

.was-validated .form-outline .form-control:valid:focus~.form-notch .form-notch-middle,
.was-validated .form-outline .form-control:valid.active~.form-notch .form-notch-middle,
.form-outline .form-control.is-valid:focus~.form-notch .form-notch-middle,
.form-outline .form-control.is-valid.active~.form-notch .form-notch-middle {
    border-top: 1px solid rgba(0, 0, 0, 0)
}

.was-validated .form-outline .form-control:valid:focus~.form-notch .form-notch-middle,
.form-outline .form-control.is-valid:focus~.form-notch .form-notch-middle {
    box-shadow: 0 1px 0 0 #14a44d
}

.was-validated .form-outline .form-control:valid:focus~.form-notch .form-notch-leading,
.form-outline .form-control.is-valid:focus~.form-notch .form-notch-leading {
    box-shadow: -1px 0 0 0 #14a44d, 0 1px 0 0 #14a44d, 0 -1px 0 0 #14a44d
}

.was-validated .form-outline .form-control:valid:focus~.form-notch .form-notch-trailing,
.form-outline .form-control.is-valid:focus~.form-notch .form-notch-trailing {
    box-shadow: 1px 0 0 0 #14a44d, 0 -1px 0 0 #14a44d, 0 1px 0 0 #14a44d
}

.was-validated .form-outline .form-control:valid.select-input.focused~.form-notch .form-notch-leading,
.form-outline .form-control.is-valid.select-input.focused~.form-notch .form-notch-leading {
    box-shadow: -1px 0 0 0 #14a44d, 0 1px 0 0 #14a44d, 0 -1px 0 0 #14a44d
}

.was-validated .form-outline .form-control:valid.select-input.focused~.form-notch .form-notch-middle,
.form-outline .form-control.is-valid.select-input.focused~.form-notch .form-notch-middle {
    box-shadow: 0 1px 0 0 #14a44d;
    border-top: 1px solid rgba(0, 0, 0, 0)
}

.was-validated .form-outline .form-control:valid.select-input.focused~.form-notch .form-notch-trailing,
.form-outline .form-control.is-valid.select-input.focused~.form-notch .form-notch-trailing {
    box-shadow: 1px 0 0 0 #14a44d, 0 -1px 0 0 #14a44d, 0 1px 0 0 #14a44d
}

.was-validated .form-select:valid,
.form-select.is-valid {
    border-color: #14a44d
}

.was-validated .form-select:valid:focus,
.form-select.is-valid:focus {
    border-color: #14a44d;
    box-shadow: 0 0 0 .25rem rgba(20, 164, 77, .25)
}

.was-validated .form-select:valid~.valid-feedback,
.form-select.is-valid~.valid-feedback {
    margin-top: 0
}

.was-validated .input-group .form-control:valid,
.input-group .form-control.is-valid {
    margin-bottom: 0
}

.was-validated input[type=file].form-control:valid .valid-feedback,
input[type=file].form-control.is-valid .valid-feedback {
    margin-top: 0
}

.was-validated input[type=file].form-control:valid:focus,
input[type=file].form-control.is-valid:focus {
    box-shadow: inset 0 0 0 1px #14a44d;
    border-color: #14a44d
}

.was-validated input[type=file].form-control:valid:focus~.form-file-label,
input[type=file].form-control.is-valid:focus~.form-file-label {
    box-shadow: none
}

.was-validated input[type=file].form-control:valid:focus-within~.form-file-label .form-file-text,
.was-validated input[type=file].form-control:valid:focus-within~.form-file-label .form-file-button,
input[type=file].form-control.is-valid:focus-within~.form-file-label .form-file-text,
input[type=file].form-control.is-valid:focus-within~.form-file-label .form-file-button {
    border-color: #14a44d
}

.was-validated .form-check-input:valid,
.form-check-input.is-valid {
    border-color: #14a44d
}

.was-validated .form-check-input:valid:checked,
.form-check-input.is-valid:checked {
    background-color: #14a44d
}

.was-validated .form-check-input:valid:checked:focus:before,
.form-check-input.is-valid:checked:focus:before {
    box-shadow: 0px 0px 0px 13px #14a44d
}

.was-validated .form-check-input:valid:focus,
.form-check-input.is-valid:focus {
    box-shadow: none
}

.was-validated .form-check-input:valid:focus:before,
.form-check-input.is-valid:focus:before {
    box-shadow: 0px 0px 0px 13px #14a44d
}

.was-validated .form-check-input:valid~.form-check-label,
.form-check-input.is-valid~.form-check-label {
    color: #14a44d;
    margin-bottom: 1rem
}

.was-validated .form-check-input:valid[type=checkbox]:checked:focus,
.form-check-input.is-valid[type=checkbox]:checked:focus {
    background-color: #14a44d;
    border-color: #14a44d
}

.was-validated .form-check-input:valid[type=radio]:checked,
.form-check-input.is-valid[type=radio]:checked {
    border-color: #14a44d;
    background-color: #fff
}

.was-validated .form-check-input:valid[type=radio]:checked:focus:before,
.form-check-input.is-valid[type=radio]:checked:focus:before {
    box-shadow: 0px 0px 0px 13px #14a44d
}

.was-validated .form-check-input:valid[type=radio]:checked:after,
.form-check-input.is-valid[type=radio]:checked:after {
    border-color: #14a44d;
    background-color: #14a44d
}

.form-check-inline .form-check-input~.valid-feedback {
    margin-left: .5em
}

.was-validated .form-switch .form-check-input:valid:focus:before,
.form-switch .form-check-input.is-valid:focus:before {
    box-shadow: 3px -1px 0px 13px rgba(var(--mdb-box-shadow-color-rgb), 0.6)
}

.was-validated .form-switch .form-check-input:valid:checked[type=checkbox]:after,
.form-switch .form-check-input.is-valid:checked[type=checkbox]:after {
    background-color: #14a44d;
    box-shadow: 0 3px 1px -2px rgba(var(--mdb-box-shadow-color-rgb), 0.2), 0 2px 2px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.14), 0 1px 5px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.12)
}

.was-validated .form-switch .form-check-input:valid:checked:focus:before,
.form-switch .form-check-input.is-valid:checked:focus:before {
    box-shadow: 3px -1px 0px 13px #14a44d
}

.invalid-feedback {
    position: absolute;
    display: none;
    width: auto;
    margin-top: .25rem;
    font-size: .875rem;
    color: #dc4c64;
    margin-top: -0.75rem
}

.invalid-tooltip {
    position: absolute;
    top: 100%;
    z-index: 5;
    display: none;
    max-width: 100%;
    padding: 6px 16px;
    margin-top: .1rem;
    font-size: .875rem;
    background-color: rgba(220, 76, 100, .9);
    border-radius: .25rem !important;
    color: #fff
}

.was-validated :invalid~.invalid-feedback,
.was-validated :invalid~.invalid-tooltip,
.is-invalid~.invalid-feedback,
.is-invalid~.invalid-tooltip {
    display: block
}

.was-validated .form-control:invalid,
.form-control.is-invalid {
    margin-bottom: 1rem;
    background-image: none;
    border-color: #dc4c64
}

.was-validated .form-control:invalid:focus,
.form-control.is-invalid:focus {
    border-color: #dc4c64;
    box-shadow: 0 0 0 .25rem rgba(220, 76, 100, .25)
}

.was-validated .form-outline .form-control:invalid~.form-label,
.form-outline .form-control.is-invalid~.form-label {
    color: #dc4c64
}

.was-validated .form-outline .form-control:invalid~.form-notch .form-notch-leading,
.was-validated .form-outline .form-control:invalid~.form-notch .form-notch-middle,
.was-validated .form-outline .form-control:invalid~.form-notch .form-notch-trailing,
.form-outline .form-control.is-invalid~.form-notch .form-notch-leading,
.form-outline .form-control.is-invalid~.form-notch .form-notch-middle,
.form-outline .form-control.is-invalid~.form-notch .form-notch-trailing {
    border-color: #dc4c64
}

.was-validated .form-outline .form-control:invalid:focus~.form-notch .form-notch-middle,
.was-validated .form-outline .form-control:invalid.active~.form-notch .form-notch-middle,
.form-outline .form-control.is-invalid:focus~.form-notch .form-notch-middle,
.form-outline .form-control.is-invalid.active~.form-notch .form-notch-middle {
    border-top: 1px solid rgba(0, 0, 0, 0)
}

.was-validated .form-outline .form-control:invalid:focus~.form-notch .form-notch-middle,
.form-outline .form-control.is-invalid:focus~.form-notch .form-notch-middle {
    box-shadow: 0 1px 0 0 #dc4c64
}

.was-validated .form-outline .form-control:invalid:focus~.form-notch .form-notch-leading,
.form-outline .form-control.is-invalid:focus~.form-notch .form-notch-leading {
    box-shadow: -1px 0 0 0 #dc4c64, 0 1px 0 0 #dc4c64, 0 -1px 0 0 #dc4c64
}

.was-validated .form-outline .form-control:invalid:focus~.form-notch .form-notch-trailing,
.form-outline .form-control.is-invalid:focus~.form-notch .form-notch-trailing {
    box-shadow: 1px 0 0 0 #dc4c64, 0 -1px 0 0 #dc4c64, 0 1px 0 0 #dc4c64
}

.was-validated .form-outline .form-control:invalid.select-input.focused~.form-notch .form-notch-leading,
.form-outline .form-control.is-invalid.select-input.focused~.form-notch .form-notch-leading {
    box-shadow: -1px 0 0 0 #dc4c64, 0 1px 0 0 #dc4c64, 0 -1px 0 0 #dc4c64
}

.was-validated .form-outline .form-control:invalid.select-input.focused~.form-notch .form-notch-middle,
.form-outline .form-control.is-invalid.select-input.focused~.form-notch .form-notch-middle {
    box-shadow: 0 1px 0 0 #dc4c64;
    border-top: 1px solid rgba(0, 0, 0, 0)
}

.was-validated .form-outline .form-control:invalid.select-input.focused~.form-notch .form-notch-trailing,
.form-outline .form-control.is-invalid.select-input.focused~.form-notch .form-notch-trailing {
    box-shadow: 1px 0 0 0 #dc4c64, 0 -1px 0 0 #dc4c64, 0 1px 0 0 #dc4c64
}

.was-validated .form-select:invalid,
.form-select.is-invalid {
    border-color: #dc4c64
}

.was-validated .form-select:invalid:focus,
.form-select.is-invalid:focus {
    border-color: #dc4c64;
    box-shadow: 0 0 0 .25rem rgba(220, 76, 100, .25)
}

.was-validated .form-select:invalid~.invalid-feedback,
.form-select.is-invalid~.invalid-feedback {
    margin-top: 0
}

.was-validated .input-group .form-control:invalid,
.input-group .form-control.is-invalid {
    margin-bottom: 0
}

.was-validated input[type=file].form-control:invalid .invalid-feedback,
input[type=file].form-control.is-invalid .invalid-feedback {
    margin-top: 0
}

.was-validated input[type=file].form-control:invalid:focus,
input[type=file].form-control.is-invalid:focus {
    box-shadow: inset 0 0 0 1px #dc4c64;
    border-color: #dc4c64
}

.was-validated input[type=file].form-control:invalid:focus~.form-file-label,
input[type=file].form-control.is-invalid:focus~.form-file-label {
    box-shadow: none
}

.was-validated input[type=file].form-control:invalid:focus-within~.form-file-label .form-file-text,
.was-validated input[type=file].form-control:invalid:focus-within~.form-file-label .form-file-button,
input[type=file].form-control.is-invalid:focus-within~.form-file-label .form-file-text,
input[type=file].form-control.is-invalid:focus-within~.form-file-label .form-file-button {
    border-color: #dc4c64
}

.was-validated .form-check-input:invalid,
.form-check-input.is-invalid {
    border-color: #dc4c64
}

.was-validated .form-check-input:invalid:checked,
.form-check-input.is-invalid:checked {
    background-color: #dc4c64
}

.was-validated .form-check-input:invalid:checked:focus:before,
.form-check-input.is-invalid:checked:focus:before {
    box-shadow: 0px 0px 0px 13px #dc4c64
}

.was-validated .form-check-input:invalid:focus,
.form-check-input.is-invalid:focus {
    box-shadow: none
}

.was-validated .form-check-input:invalid:focus:before,
.form-check-input.is-invalid:focus:before {
    box-shadow: 0px 0px 0px 13px #dc4c64
}

.was-validated .form-check-input:invalid~.form-check-label,
.form-check-input.is-invalid~.form-check-label {
    color: #dc4c64;
    margin-bottom: 1rem
}

.was-validated .form-check-input:invalid[type=checkbox]:checked:focus,
.form-check-input.is-invalid[type=checkbox]:checked:focus {
    background-color: #dc4c64;
    border-color: #dc4c64
}

.was-validated .form-check-input:invalid[type=radio]:checked,
.form-check-input.is-invalid[type=radio]:checked {
    border-color: #dc4c64;
    background-color: #fff
}

.was-validated .form-check-input:invalid[type=radio]:checked:focus:before,
.form-check-input.is-invalid[type=radio]:checked:focus:before {
    box-shadow: 0px 0px 0px 13px #dc4c64
}

.was-validated .form-check-input:invalid[type=radio]:checked:after,
.form-check-input.is-invalid[type=radio]:checked:after {
    border-color: #dc4c64;
    background-color: #dc4c64
}

.form-check-inline .form-check-input~.invalid-feedback {
    margin-left: .5em
}

.was-validated .form-switch .form-check-input:invalid:focus:before,
.form-switch .form-check-input.is-invalid:focus:before {
    box-shadow: 3px -1px 0px 13px rgba(var(--mdb-box-shadow-color-rgb), 0.6)
}

.was-validated .form-switch .form-check-input:invalid:checked[type=checkbox]:after,
.form-switch .form-check-input.is-invalid:checked[type=checkbox]:after {
    background-color: #dc4c64;
    box-shadow: 0 3px 1px -2px rgba(var(--mdb-box-shadow-color-rgb), 0.2), 0 2px 2px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.14), 0 1px 5px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.12)
}

.was-validated .form-switch .form-check-input:invalid:checked:focus:before,
.form-switch .form-check-input.is-invalid:checked:focus:before {
    box-shadow: 3px -1px 0px 13px #dc4c64
}

.form-range:focus {
    box-shadow: none
}

.form-range:focus::-webkit-slider-thumb {
    box-shadow: none
}

.form-range:focus::-moz-range-thumb {
    box-shadow: none
}

.form-range:focus::-ms-thumb {
    box-shadow: none
}

.form-range::-moz-focus-outer {
    border: 0
}

.form-range::-webkit-slider-thumb {
    margin-top: -6px;
    box-shadow: none;
    appearance: none
}

.form-range::-webkit-slider-runnable-track {
    height: 4px;
    border-radius: 0;
    box-shadow: none;
    background-color: var(--mdb-secondary-bg)
}

.form-range::-moz-range-thumb {
    box-shadow: none;
    appearance: none
}

.form-range::-moz-range-track {
    box-shadow: none
}

.table {
    --mdb-table-font-size: 0.9rem;
    --mdb-table-divider-color: currentcolor;
    font-size: var(--mdb-table-font-size)
}

.table th {
    font-weight: 500
}

.table tbody {
    font-weight: 400
}

.table>:not(:last-child)>:last-child>* {
    border-bottom-color: inherit
}

.table-primary {
    --mdb-table-color: #000;
    --mdb-table-bg: #d8e3f4;
    --mdb-table-border-color: #adb6c3;
    --mdb-table-striped-bg: #cdd8e8;
    --mdb-table-striped-color: #000;
    --mdb-table-active-bg: #c2ccdc;
    --mdb-table-active-color: #000;
    --mdb-table-hover-bg: #c8d2e2;
    --mdb-table-hover-color: #000;
    color: var(--mdb-table-color);
    border-color: var(--mdb-table-border-color)
}

.table-secondary {
    --mdb-table-color: #000;
    --mdb-table-bg: #ecedf0;
    --mdb-table-border-color: #bdbec0;
    --mdb-table-striped-bg: #e0e1e4;
    --mdb-table-striped-color: #000;
    --mdb-table-active-bg: #d4d5d8;
    --mdb-table-active-color: #000;
    --mdb-table-hover-bg: #dadbde;
    --mdb-table-hover-color: #000;
    color: var(--mdb-table-color);
    border-color: var(--mdb-table-border-color)
}

.table-success {
    --mdb-table-color: #000;
    --mdb-table-bg: #d0eddb;
    --mdb-table-border-color: #a6beaf;
    --mdb-table-striped-bg: #c6e1d0;
    --mdb-table-striped-color: #000;
    --mdb-table-active-bg: #bbd5c5;
    --mdb-table-active-color: #000;
    --mdb-table-hover-bg: #c0dbcb;
    --mdb-table-hover-color: #000;
    color: var(--mdb-table-color);
    border-color: var(--mdb-table-border-color)
}

.table-info {
    --mdb-table-color: #000;
    --mdb-table-bg: #ddf0f6;
    --mdb-table-border-color: #b1c0c5;
    --mdb-table-striped-bg: #d2e4ea;
    --mdb-table-striped-color: #000;
    --mdb-table-active-bg: #c7d8dd;
    --mdb-table-active-color: #000;
    --mdb-table-hover-bg: #ccdee4;
    --mdb-table-hover-color: #000;
    color: var(--mdb-table-color);
    border-color: var(--mdb-table-border-color)
}

.table-warning {
    --mdb-table-color: #000;
    --mdb-table-bg: #faecd1;
    --mdb-table-border-color: #c8bda7;
    --mdb-table-striped-bg: #eee0c7;
    --mdb-table-striped-color: #000;
    --mdb-table-active-bg: #e1d4bc;
    --mdb-table-active-color: #000;
    --mdb-table-hover-bg: #e7dac1;
    --mdb-table-hover-color: #000;
    color: var(--mdb-table-color);
    border-color: var(--mdb-table-border-color)
}

.table-danger {
    --mdb-table-color: #000;
    --mdb-table-bg: #f8dbe0;
    --mdb-table-border-color: #c6afb3;
    --mdb-table-striped-bg: #ecd0d5;
    --mdb-table-striped-color: #000;
    --mdb-table-active-bg: #dfc5ca;
    --mdb-table-active-color: #000;
    --mdb-table-hover-bg: #e5cbcf;
    --mdb-table-hover-color: #000;
    color: var(--mdb-table-color);
    border-color: var(--mdb-table-border-color)
}

.table-light {
    --mdb-table-color: #000;
    --mdb-table-bg: #fbfbfb;
    --mdb-table-border-color: #c9c9c9;
    --mdb-table-striped-bg: #eeeeee;
    --mdb-table-striped-color: #000;
    --mdb-table-active-bg: #e2e2e2;
    --mdb-table-active-color: #000;
    --mdb-table-hover-bg: #e8e8e8;
    --mdb-table-hover-color: #000;
    color: var(--mdb-table-color);
    border-color: var(--mdb-table-border-color)
}

.table-dark {
    --mdb-table-color: #fff;
    --mdb-table-bg: #332d2d;
    --mdb-table-border-color: #5c5757;
    --mdb-table-striped-bg: #3d3838;
    --mdb-table-striped-color: #fff;
    --mdb-table-active-bg: #474242;
    --mdb-table-active-color: #fff;
    --mdb-table-hover-bg: #423d3d;
    --mdb-table-hover-color: #fff;
    color: var(--mdb-table-color);
    border-color: var(--mdb-table-border-color)
}

.table-hover>tbody>tr {
    transition: .5s
}

.table-hover>tbody>tr:hover {
    --mdb-table-accent-bg: transparent;
    background-color: var(--mdb-table-hover-bg)
}

.table-group-divider {
    border-top: calc(2*var(--mdb-border-width)) solid;
    border-top-color: inherit
}

.table-divider-color {
    border-top-color: var(--mdb-table-divider-color)
}

.btn {
    --mdb-btn-padding-top: 0.625rem;
    --mdb-btn-padding-bottom: 0.5rem;
    --mdb-btn-border-width: 0;
    --mdb-btn-border-color: none;
    --mdb-btn-border-radius: 0.25rem;
    --mdb-btn-box-shadow: 0 4px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.35);
    --mdb-btn-hover-box-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-focus-box-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-active-box-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    padding-top: var(--mdb-btn-padding-top);
    padding-bottom: var(--mdb-btn-padding-bottom);
    text-transform: uppercase;
    vertical-align: bottom;
    border: 0;
    border-radius: var(--mdb-btn-border-radius);
    box-shadow: var(--mdb-btn-box-shadow)
}

:not(.btn-check)+.btn:hover,
.btn:first-child:hover,
.btn:focus-visible,
.btn:hover {
    box-shadow: var(--mdb-btn-hover-box-shadow)
}

.btn-check:focus-visible+.btn,
.btn-check:focus+.btn,
.btn:focus {
    box-shadow: var(--mdb-btn-focus-box-shadow)
}

.btn-check:checked+.btn,
.btn-check:active+.btn,
.btn:active,
.btn.active,
.btn.show {
    box-shadow: var(--mdb-btn-active-box-shadow)
}

.btn-check:checked+.btn:focus,
.btn-check:active+.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.show:focus {
    box-shadow: var(--mdb-btn-focus-box-shadow)
}

.btn:disabled,
.btn.disabled,
fieldset:disabled .btn {
    box-shadow: var(--mdb-btn-box-shadow)
}

[class*=btn-outline-] {
    --mdb-btn-padding-top: 0.5rem;
    --mdb-btn-padding-bottom: 0.375rem;
    --mdb-btn-padding-x: 1.375rem;
    --mdb-btn-border-width: 2px;
    --mdb-btn-line-height: 1.5;
    padding: var(--mdb-btn-padding-top) var(--mdb-btn-padding-x) var(--mdb-btn-padding-bottom);
    border-width: var(--mdb-btn-border-width);
    border-style: solid;
    box-shadow: none
}

:not(.btn-check)+[class*=btn-outline-]:hover,
[class*=btn-outline-]:first-child:hover,
[class*=btn-outline-]:focus-visible,
[class*=btn-outline-]:hover {
    box-shadow: none
}

.btn-check:focus-visible+[class*=btn-outline-],
.btn-check:focus+[class*=btn-outline-],
[class*=btn-outline-]:focus {
    box-shadow: none
}

.btn-check:checked+[class*=btn-outline-],
.btn-check:active+[class*=btn-outline-],
[class*=btn-outline-]:active,
[class*=btn-outline-].active,
[class*=btn-outline-].show {
    box-shadow: none
}

.btn-check:checked+[class*=btn-outline-]:focus,
.btn-check:active+[class*=btn-outline-]:focus,
[class*=btn-outline-]:active:focus,
[class*=btn-outline-].active:focus,
[class*=btn-outline-].show:focus {
    box-shadow: none
}

[class*=btn-outline-]:disabled,
[class*=btn-outline-].disabled,
fieldset:disabled [class*=btn-outline-] {
    box-shadow: none
}

[class*=btn-outline-].btn-lg,
.btn-group-lg>[class*=btn-outline-].btn {
    --mdb-btn-padding-top: 0.625rem;
    --mdb-btn-padding-bottom: 0.5625rem;
    --mdb-btn-padding-x: 1.5625rem;
    --mdb-btn-font-size: 0.875rem;
    --mdb-btn-line-height: 1.6
}

[class*=btn-outline-].btn-sm,
.btn-group-sm>[class*=btn-outline-].btn {
    --mdb-btn-padding-top: 0.25rem;
    --mdb-btn-padding-bottom: 0.1875rem;
    --mdb-btn-padding-x: 0.875rem;
    --mdb-btn-font-size: 0.75rem;
    --mdb-btn-line-height: 1.5
}

.btn-secondary {
    box-shadow: none
}

:not(.btn-check)+.btn-secondary:hover,
.btn-secondary:first-child:hover,
.btn-secondary:focus-visible,
.btn-secondary:hover {
    box-shadow: none !important
}

.btn-check:focus-visible+.btn-secondary,
.btn-check:focus+.btn-secondary,
.btn-secondary:focus {
    box-shadow: none
}

.btn-check:checked+.btn-secondary,
.btn-check:active+.btn-secondary,
.btn-secondary:active,
.btn-secondary.active,
.btn-secondary.show {
    box-shadow: none
}

.btn-check:checked+.btn-secondary:focus,
.btn-check:active+.btn-secondary:focus,
.btn-secondary:active:focus,
.btn-secondary.active:focus,
.btn-secondary.show:focus {
    box-shadow: none
}

.btn-secondary:disabled,
.btn-secondary.disabled,
fieldset:disabled .btn-secondary {
    box-shadow: none
}

.btn-primary {
    --mdb-btn-bg: #3b71ca;
    --mdb-btn-color: #fff;
    --mdb-btn-box-shadow: 0 4px 9px -4px #386bc0;
    --mdb-btn-hover-bg: #386bc0;
    --mdb-btn-hover-color: #fff;
    --mdb-btn-focus-bg: #386bc0;
    --mdb-btn-focus-color: #fff;
    --mdb-btn-active-bg: #3566b6;
    --mdb-btn-active-color: #fff;
    --mdb-btn-box-shadow-state: 0 8px 9px -4px rgba(56, 107, 192, 0.3), 0 4px 18px 0 rgba(56, 107, 192, 0.2)
}

:not(.btn-check)+.btn-primary:hover,
.btn-primary:first-child:hover,
.btn-primary:focus-visible,
.btn-primary:hover {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:focus-visible+.btn-primary,
.btn-check:focus+.btn-primary,
.btn-primary:focus {
    box-shadow: var(--mdb-btn-box-shadow-state);
    background-color: var(--mdb-btn-focus-bg)
}

.btn-check:checked+.btn-primary,
.btn-check:active+.btn-primary,
.btn-primary:active,
.btn-primary.active,
.btn-primary.show {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:checked+.btn-primary:focus,
.btn-check:active+.btn-primary:focus,
.btn-primary:active:focus,
.btn-primary.active:focus,
.btn-primary.show:focus {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:checked+.btn-primary:hover,
.btn-check:active+.btn-primary:hover,
.btn-primary:active:hover,
.btn-primary.active:hover,
.btn-primary.show:hover {
    background-color: var(--mdb-btn-active-bg)
}

.btn-primary:disabled,
.btn-primary.disabled,
fieldset:disabled .btn-primary {
    box-shadow: var(--mdb-btn-box-shadow)
}

[data-mdb-theme=dark] .btn-primary {
    box-shadow: 0 4px 9px -4px rgba(0, 0, 0, .35)
}

[data-mdb-theme=dark] .btn-primary:hover,
[data-mdb-theme=dark] .btn-primary:active,
[data-mdb-theme=dark] .btn-primary:focus {
    box-shadow: 0 4px 18px -2px rgba(0, 0, 0, .7)
}

.btn-secondary {
    --mdb-btn-bg: #e2eaf7;
    --mdb-btn-color: #294f8d;
    --mdb-btn-box-shadow: 0 4px 9px -4px #e3ebf7;
    --mdb-btn-hover-bg: #d7deeb;
    --mdb-btn-hover-color: #294f8d;
    --mdb-btn-focus-bg: #d7deeb;
    --mdb-btn-focus-color: #294f8d;
    --mdb-btn-active-bg: #d7deeb;
    --mdb-btn-active-color: #294f8d;
    --mdb-btn-box-shadow-state: transparent
}

:not(.btn-check)+.btn-secondary:hover,
.btn-secondary:first-child:hover,
.btn-secondary:focus-visible,
.btn-secondary:hover {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:focus-visible+.btn-secondary,
.btn-check:focus+.btn-secondary,
.btn-secondary:focus {
    box-shadow: var(--mdb-btn-box-shadow-state);
    background-color: var(--mdb-btn-focus-bg)
}

.btn-check:checked+.btn-secondary,
.btn-check:active+.btn-secondary,
.btn-secondary:active,
.btn-secondary.active,
.btn-secondary.show {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:checked+.btn-secondary:focus,
.btn-check:active+.btn-secondary:focus,
.btn-secondary:active:focus,
.btn-secondary.active:focus,
.btn-secondary.show:focus {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:checked+.btn-secondary:hover,
.btn-check:active+.btn-secondary:hover,
.btn-secondary:active:hover,
.btn-secondary.active:hover,
.btn-secondary.show:hover {
    background-color: var(--mdb-btn-active-bg)
}

.btn-secondary:disabled,
.btn-secondary.disabled,
fieldset:disabled .btn-secondary {
    box-shadow: var(--mdb-btn-box-shadow)
}

.btn-success {
    --mdb-btn-bg: #14a44d;
    --mdb-btn-color: #fff;
    --mdb-btn-box-shadow: 0 4px 9px -4px #139c49;
    --mdb-btn-hover-bg: #139c49;
    --mdb-btn-hover-color: #fff;
    --mdb-btn-focus-bg: #139c49;
    --mdb-btn-focus-color: #fff;
    --mdb-btn-active-bg: #129445;
    --mdb-btn-active-color: #fff;
    --mdb-btn-box-shadow-state: 0 8px 9px -4px rgba(19, 156, 73, 0.3), 0 4px 18px 0 rgba(19, 156, 73, 0.2)
}

:not(.btn-check)+.btn-success:hover,
.btn-success:first-child:hover,
.btn-success:focus-visible,
.btn-success:hover {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:focus-visible+.btn-success,
.btn-check:focus+.btn-success,
.btn-success:focus {
    box-shadow: var(--mdb-btn-box-shadow-state);
    background-color: var(--mdb-btn-focus-bg)
}

.btn-check:checked+.btn-success,
.btn-check:active+.btn-success,
.btn-success:active,
.btn-success.active,
.btn-success.show {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:checked+.btn-success:focus,
.btn-check:active+.btn-success:focus,
.btn-success:active:focus,
.btn-success.active:focus,
.btn-success.show:focus {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:checked+.btn-success:hover,
.btn-check:active+.btn-success:hover,
.btn-success:active:hover,
.btn-success.active:hover,
.btn-success.show:hover {
    background-color: var(--mdb-btn-active-bg)
}

.btn-success:disabled,
.btn-success.disabled,
fieldset:disabled .btn-success {
    box-shadow: var(--mdb-btn-box-shadow)
}

[data-mdb-theme=dark] .btn-success {
    box-shadow: 0 4px 9px -4px rgba(0, 0, 0, .35)
}

[data-mdb-theme=dark] .btn-success:hover,
[data-mdb-theme=dark] .btn-success:active,
[data-mdb-theme=dark] .btn-success:focus {
    box-shadow: 0 4px 18px -2px rgba(0, 0, 0, .7)
}

.btn-danger {
    --mdb-btn-bg: #dc4c64;
    --mdb-btn-color: #fff;
    --mdb-btn-box-shadow: 0 4px 9px -4px #d1485f;
    --mdb-btn-hover-bg: #d1485f;
    --mdb-btn-hover-color: #fff;
    --mdb-btn-focus-bg: #d1485f;
    --mdb-btn-focus-color: #fff;
    --mdb-btn-active-bg: #c6445a;
    --mdb-btn-active-color: #fff;
    --mdb-btn-box-shadow-state: 0 8px 9px -4px rgba(209, 72, 95, 0.3), 0 4px 18px 0 rgba(209, 72, 95, 0.2)
}

:not(.btn-check)+.btn-danger:hover,
.btn-danger:first-child:hover,
.btn-danger:focus-visible,
.btn-danger:hover {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:focus-visible+.btn-danger,
.btn-check:focus+.btn-danger,
.btn-danger:focus {
    box-shadow: var(--mdb-btn-box-shadow-state);
    background-color: var(--mdb-btn-focus-bg)
}

.btn-check:checked+.btn-danger,
.btn-check:active+.btn-danger,
.btn-danger:active,
.btn-danger.active,
.btn-danger.show {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:checked+.btn-danger:focus,
.btn-check:active+.btn-danger:focus,
.btn-danger:active:focus,
.btn-danger.active:focus,
.btn-danger.show:focus {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:checked+.btn-danger:hover,
.btn-check:active+.btn-danger:hover,
.btn-danger:active:hover,
.btn-danger.active:hover,
.btn-danger.show:hover {
    background-color: var(--mdb-btn-active-bg)
}

.btn-danger:disabled,
.btn-danger.disabled,
fieldset:disabled .btn-danger {
    box-shadow: var(--mdb-btn-box-shadow)
}

[data-mdb-theme=dark] .btn-danger {
    box-shadow: 0 4px 9px -4px rgba(0, 0, 0, .35)
}

[data-mdb-theme=dark] .btn-danger:hover,
[data-mdb-theme=dark] .btn-danger:active,
[data-mdb-theme=dark] .btn-danger:focus {
    box-shadow: 0 4px 18px -2px rgba(0, 0, 0, .7)
}

.btn-warning {
    --mdb-btn-bg: #e4a11b;
    --mdb-btn-color: #fff;
    --mdb-btn-box-shadow: 0 4px 9px -4px #d9991a;
    --mdb-btn-hover-bg: #d9991a;
    --mdb-btn-hover-color: #fff;
    --mdb-btn-focus-bg: #d9991a;
    --mdb-btn-focus-color: #fff;
    --mdb-btn-active-bg: #cd9118;
    --mdb-btn-active-color: #fff;
    --mdb-btn-box-shadow-state: 0 8px 9px -4px rgba(217, 153, 26, 0.3), 0 4px 18px 0 rgba(217, 153, 26, 0.2)
}

:not(.btn-check)+.btn-warning:hover,
.btn-warning:first-child:hover,
.btn-warning:focus-visible,
.btn-warning:hover {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:focus-visible+.btn-warning,
.btn-check:focus+.btn-warning,
.btn-warning:focus {
    box-shadow: var(--mdb-btn-box-shadow-state);
    background-color: var(--mdb-btn-focus-bg)
}

.btn-check:checked+.btn-warning,
.btn-check:active+.btn-warning,
.btn-warning:active,
.btn-warning.active,
.btn-warning.show {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:checked+.btn-warning:focus,
.btn-check:active+.btn-warning:focus,
.btn-warning:active:focus,
.btn-warning.active:focus,
.btn-warning.show:focus {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:checked+.btn-warning:hover,
.btn-check:active+.btn-warning:hover,
.btn-warning:active:hover,
.btn-warning.active:hover,
.btn-warning.show:hover {
    background-color: var(--mdb-btn-active-bg)
}

.btn-warning:disabled,
.btn-warning.disabled,
fieldset:disabled .btn-warning {
    box-shadow: var(--mdb-btn-box-shadow)
}

[data-mdb-theme=dark] .btn-warning {
    box-shadow: 0 4px 9px -4px rgba(0, 0, 0, .35)
}

[data-mdb-theme=dark] .btn-warning:hover,
[data-mdb-theme=dark] .btn-warning:active,
[data-mdb-theme=dark] .btn-warning:focus {
    box-shadow: 0 4px 18px -2px rgba(0, 0, 0, .7)
}

.btn-info {
    --mdb-btn-bg: #54b4d3;
    --mdb-btn-color: #fff;
    --mdb-btn-box-shadow: 0 4px 9px -4px #50abc8;
    --mdb-btn-hover-bg: #50abc8;
    --mdb-btn-hover-color: #fff;
    --mdb-btn-focus-bg: #50abc8;
    --mdb-btn-focus-color: #fff;
    --mdb-btn-active-bg: #4ca2be;
    --mdb-btn-active-color: #fff;
    --mdb-btn-box-shadow-state: 0 8px 9px -4px rgba(80, 171, 200, 0.3), 0 4px 18px 0 rgba(80, 171, 200, 0.2)
}

:not(.btn-check)+.btn-info:hover,
.btn-info:first-child:hover,
.btn-info:focus-visible,
.btn-info:hover {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:focus-visible+.btn-info,
.btn-check:focus+.btn-info,
.btn-info:focus {
    box-shadow: var(--mdb-btn-box-shadow-state);
    background-color: var(--mdb-btn-focus-bg)
}

.btn-check:checked+.btn-info,
.btn-check:active+.btn-info,
.btn-info:active,
.btn-info.active,
.btn-info.show {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:checked+.btn-info:focus,
.btn-check:active+.btn-info:focus,
.btn-info:active:focus,
.btn-info.active:focus,
.btn-info.show:focus {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:checked+.btn-info:hover,
.btn-check:active+.btn-info:hover,
.btn-info:active:hover,
.btn-info.active:hover,
.btn-info.show:hover {
    background-color: var(--mdb-btn-active-bg)
}

.btn-info:disabled,
.btn-info.disabled,
fieldset:disabled .btn-info {
    box-shadow: var(--mdb-btn-box-shadow)
}

[data-mdb-theme=dark] .btn-info {
    box-shadow: 0 4px 9px -4px rgba(0, 0, 0, .35)
}

[data-mdb-theme=dark] .btn-info:hover,
[data-mdb-theme=dark] .btn-info:active,
[data-mdb-theme=dark] .btn-info:focus {
    box-shadow: 0 4px 18px -2px rgba(0, 0, 0, .7)
}

.btn-light {
    --mdb-btn-bg: #f5f5f5;
    --mdb-btn-color: #616161;
    --mdb-btn-box-shadow: 0 4px 9px -4px #f6f6f6;
    --mdb-btn-hover-bg: #e9e9e9;
    --mdb-btn-hover-color: #616161;
    --mdb-btn-focus-bg: #f6f6f6;
    --mdb-btn-focus-color: #616161;
    --mdb-btn-active-bg: #dddddd;
    --mdb-btn-active-color: #616161;
    --mdb-btn-box-shadow-state: 0 8px 9px -4px rgba(238, 238, 238, 0.3), 0 4px 18px 0 rgba(238, 238, 238, 0.2)
}

:not(.btn-check)+.btn-light:hover,
.btn-light:first-child:hover,
.btn-light:focus-visible,
.btn-light:hover {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:focus-visible+.btn-light,
.btn-check:focus+.btn-light,
.btn-light:focus {
    box-shadow: var(--mdb-btn-box-shadow-state);
    background-color: var(--mdb-btn-focus-bg)
}

.btn-check:checked+.btn-light,
.btn-check:active+.btn-light,
.btn-light:active,
.btn-light.active,
.btn-light.show {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:checked+.btn-light:focus,
.btn-check:active+.btn-light:focus,
.btn-light:active:focus,
.btn-light.active:focus,
.btn-light.show:focus {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:checked+.btn-light:hover,
.btn-check:active+.btn-light:hover,
.btn-light:active:hover,
.btn-light.active:hover,
.btn-light.show:hover {
    background-color: var(--mdb-btn-active-bg)
}

.btn-light:disabled,
.btn-light.disabled,
fieldset:disabled .btn-light {
    box-shadow: var(--mdb-btn-box-shadow)
}

[data-mdb-theme=dark] .btn-light {
    box-shadow: 0 4px 9px -4px rgba(0, 0, 0, .35)
}

[data-mdb-theme=dark] .btn-light:hover,
[data-mdb-theme=dark] .btn-light:active,
[data-mdb-theme=dark] .btn-light:focus {
    box-shadow: 0 4px 18px -2px rgba(0, 0, 0, .7)
}

.btn-dark {
    --mdb-btn-bg: #262626;
    --mdb-btn-color: #eeeeee;
    --mdb-btn-box-shadow: 0 4px 9px -4px #313131;
    --mdb-btn-hover-bg: #313131;
    --mdb-btn-hover-color: #eeeeee;
    --mdb-btn-focus-bg: #313131;
    --mdb-btn-focus-color: #eeeeee;
    --mdb-btn-active-bg: #3c3c3c;
    --mdb-btn-active-color: #eeeeee;
    --mdb-btn-box-shadow-state: 0 8px 9px -4px rgba(48, 43, 43, 0.3), 0 4px 18px 0 rgba(48, 43, 43, 0.2)
}

:not(.btn-check)+.btn-dark:hover,
.btn-dark:first-child:hover,
.btn-dark:focus-visible,
.btn-dark:hover {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:focus-visible+.btn-dark,
.btn-check:focus+.btn-dark,
.btn-dark:focus {
    box-shadow: var(--mdb-btn-box-shadow-state);
    background-color: var(--mdb-btn-focus-bg)
}

.btn-check:checked+.btn-dark,
.btn-check:active+.btn-dark,
.btn-dark:active,
.btn-dark.active,
.btn-dark.show {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:checked+.btn-dark:focus,
.btn-check:active+.btn-dark:focus,
.btn-dark:active:focus,
.btn-dark.active:focus,
.btn-dark.show:focus {
    box-shadow: var(--mdb-btn-box-shadow-state)
}

.btn-check:checked+.btn-dark:hover,
.btn-check:active+.btn-dark:hover,
.btn-dark:active:hover,
.btn-dark.active:hover,
.btn-dark.show:hover {
    background-color: var(--mdb-btn-active-bg)
}

.btn-dark:disabled,
.btn-dark.disabled,
fieldset:disabled .btn-dark {
    box-shadow: var(--mdb-btn-box-shadow)
}

[data-mdb-theme=dark] .btn-dark {
    box-shadow: 0 4px 9px -4px rgba(0, 0, 0, .35)
}

[data-mdb-theme=dark] .btn-dark:hover,
[data-mdb-theme=dark] .btn-dark:active,
[data-mdb-theme=dark] .btn-dark:focus {
    box-shadow: 0 4px 18px -2px rgba(0, 0, 0, .7)
}

.btn-outline-primary {
    --mdb-btn-bg: transparent;
    --mdb-btn-color: #3b71ca;
    --mdb-btn-hover-bg: #f5f8fc;
    --mdb-btn-hover-color: #386bc0;
    --mdb-btn-focus-bg: #f5f8fc;
    --mdb-btn-focus-color: #386bc0;
    --mdb-btn-active-bg: #f5f8fc;
    --mdb-btn-active-color: #3566b6;
    --mdb-btn-outline-border-color: #3b71ca;
    --mdb-btn-outline-focus-border-color: #2f5aa2;
    --mdb-btn-outline-hover-border-color: #2f5aa2;
    border-color: var(--mdb-btn-outline-border-color)
}

:not(.btn-check)+.btn-outline-primary:hover,
.btn-outline-primary:first-child:hover,
.btn-outline-primary:focus-visible,
.btn-outline-primary:hover {
    border-color: var(--mdb-btn-outline-hover-border-color)
}

.btn-check:focus-visible+.btn-outline-primary,
.btn-check:focus+.btn-outline-primary,
.btn-outline-primary:focus {
    border-color: var(--mdb-btn-outline-focus-border-color)
}

.btn-check:checked+.btn-outline-primary,
.btn-check:active+.btn-outline-primary,
.btn-outline-primary:active,
.btn-outline-primary.active,
.btn-outline-primary.show {
    border-color: var(--mdb-btn-outline-active-border-color)
}

.btn-check:checked+.btn-outline-primary:focus,
.btn-check:active+.btn-outline-primary:focus,
.btn-outline-primary:active:focus,
.btn-outline-primary.active:focus,
.btn-outline-primary.show:focus {
    border-color: var(--mdb-btn-outline-focus-border-color)
}

.btn-outline-primary:disabled,
.btn-outline-primary.disabled,
fieldset:disabled .btn-outline-primary {
    border-color: var(--mdb-btn-outline-border-color)
}

[data-mdb-theme=dark] .btn-outline-primary {
    --mdb-btn-bg: transparent;
    --mdb-btn-color: #628dd5;
    --mdb-btn-hover-bg: #12223d;
    --mdb-btn-hover-color: #386bc0;
    --mdb-btn-focus-bg: #12223d;
    --mdb-btn-focus-color: #386bc0;
    --mdb-btn-active-bg: #12223d;
    --mdb-btn-active-color: #3566b6
}

.btn-outline-secondary {
    --mdb-btn-bg: transparent;
    --mdb-btn-color: #294f8d;
    --mdb-btn-hover-bg: #f4f6f9;
    --mdb-btn-hover-color: #294f8d;
    --mdb-btn-focus-bg: #f4f6f9;
    --mdb-btn-focus-color: #294f8d;
    --mdb-btn-active-bg: #f4f6f9;
    --mdb-btn-active-color: #294f8d;
    --mdb-btn-outline-border-color: #e2eaf7;
    --mdb-btn-outline-focus-border-color: #d7deeb;
    --mdb-btn-outline-hover-border-color: #d7deeb;
    border-color: var(--mdb-btn-outline-border-color)
}

:not(.btn-check)+.btn-outline-secondary:hover,
.btn-outline-secondary:first-child:hover,
.btn-outline-secondary:focus-visible,
.btn-outline-secondary:hover {
    border-color: var(--mdb-btn-outline-hover-border-color)
}

.btn-check:focus-visible+.btn-outline-secondary,
.btn-check:focus+.btn-outline-secondary,
.btn-outline-secondary:focus {
    border-color: var(--mdb-btn-outline-focus-border-color)
}

.btn-check:checked+.btn-outline-secondary,
.btn-check:active+.btn-outline-secondary,
.btn-outline-secondary:active,
.btn-outline-secondary.active,
.btn-outline-secondary.show {
    border-color: var(--mdb-btn-outline-active-border-color)
}

.btn-check:checked+.btn-outline-secondary:focus,
.btn-check:active+.btn-outline-secondary:focus,
.btn-outline-secondary:active:focus,
.btn-outline-secondary.active:focus,
.btn-outline-secondary.show:focus {
    border-color: var(--mdb-btn-outline-focus-border-color)
}

.btn-outline-secondary:disabled,
.btn-outline-secondary.disabled,
fieldset:disabled .btn-outline-secondary {
    border-color: var(--mdb-btn-outline-border-color)
}

[data-mdb-theme=dark] .btn-outline-secondary {
    --mdb-btn-bg: transparent;
    --mdb-btn-color: #c4d4ef;
    --mdb-btn-hover-bg: #182d51;
    --mdb-btn-hover-color: #b1c6ea;
    --mdb-btn-focus-bg: #182d51;
    --mdb-btn-focus-color: #b1c6ea;
    --mdb-btn-active-bg: #182d51;
    --mdb-btn-active-color: #b1c6ea;
    --mdb-btn-outline-border-color: #9db8e5;
    --mdb-btn-outline-focus-border-color: #95afda;
    --mdb-btn-outline-hover-border-color: #95afda;
    border-color: var(--mdb-btn-outline-border-color)
}

.btn-outline-success {
    --mdb-btn-bg: transparent;
    --mdb-btn-color: #14a44d;
    --mdb-btn-hover-bg: #f3faf6;
    --mdb-btn-hover-color: #139c49;
    --mdb-btn-focus-bg: #f3faf6;
    --mdb-btn-focus-color: #139c49;
    --mdb-btn-active-bg: #f3faf6;
    --mdb-btn-active-color: #129445;
    --mdb-btn-outline-border-color: #14a44d;
    --mdb-btn-outline-focus-border-color: #10833e;
    --mdb-btn-outline-hover-border-color: #10833e;
    border-color: var(--mdb-btn-outline-border-color)
}

:not(.btn-check)+.btn-outline-success:hover,
.btn-outline-success:first-child:hover,
.btn-outline-success:focus-visible,
.btn-outline-success:hover {
    border-color: var(--mdb-btn-outline-hover-border-color)
}

.btn-check:focus-visible+.btn-outline-success,
.btn-check:focus+.btn-outline-success,
.btn-outline-success:focus {
    border-color: var(--mdb-btn-outline-focus-border-color)
}

.btn-check:checked+.btn-outline-success,
.btn-check:active+.btn-outline-success,
.btn-outline-success:active,
.btn-outline-success.active,
.btn-outline-success.show {
    border-color: var(--mdb-btn-outline-active-border-color)
}

.btn-check:checked+.btn-outline-success:focus,
.btn-check:active+.btn-outline-success:focus,
.btn-outline-success:active:focus,
.btn-outline-success.active:focus,
.btn-outline-success.show:focus {
    border-color: var(--mdb-btn-outline-focus-border-color)
}

.btn-outline-success:disabled,
.btn-outline-success.disabled,
fieldset:disabled .btn-outline-success {
    border-color: var(--mdb-btn-outline-border-color)
}

[data-mdb-theme=dark] .btn-outline-success {
    --mdb-btn-bg: transparent;
    --mdb-btn-color: #43b671;
    --mdb-btn-hover-bg: #063117;
    --mdb-btn-hover-color: #139c49;
    --mdb-btn-focus-bg: #063117;
    --mdb-btn-focus-color: #139c49;
    --mdb-btn-active-bg: #063117;
    --mdb-btn-active-color: #129445
}

.btn-outline-danger {
    --mdb-btn-bg: transparent;
    --mdb-btn-color: #dc4c64;
    --mdb-btn-hover-bg: #fdf6f7;
    --mdb-btn-hover-color: #d1485f;
    --mdb-btn-focus-bg: #fdf6f7;
    --mdb-btn-focus-color: #d1485f;
    --mdb-btn-active-bg: #fdf6f7;
    --mdb-btn-active-color: #c6445a;
    --mdb-btn-outline-border-color: #dc4c64;
    --mdb-btn-outline-focus-border-color: #b03d50;
    --mdb-btn-outline-hover-border-color: #b03d50;
    border-color: var(--mdb-btn-outline-border-color)
}

:not(.btn-check)+.btn-outline-danger:hover,
.btn-outline-danger:first-child:hover,
.btn-outline-danger:focus-visible,
.btn-outline-danger:hover {
    border-color: var(--mdb-btn-outline-hover-border-color)
}

.btn-check:focus-visible+.btn-outline-danger,
.btn-check:focus+.btn-outline-danger,
.btn-outline-danger:focus {
    border-color: var(--mdb-btn-outline-focus-border-color)
}

.btn-check:checked+.btn-outline-danger,
.btn-check:active+.btn-outline-danger,
.btn-outline-danger:active,
.btn-outline-danger.active,
.btn-outline-danger.show {
    border-color: var(--mdb-btn-outline-active-border-color)
}

.btn-check:checked+.btn-outline-danger:focus,
.btn-check:active+.btn-outline-danger:focus,
.btn-outline-danger:active:focus,
.btn-outline-danger.active:focus,
.btn-outline-danger.show:focus {
    border-color: var(--mdb-btn-outline-focus-border-color)
}

.btn-outline-danger:disabled,
.btn-outline-danger.disabled,
fieldset:disabled .btn-outline-danger {
    border-color: var(--mdb-btn-outline-border-color)
}

[data-mdb-theme=dark] .btn-outline-danger {
    --mdb-btn-bg: transparent;
    --mdb-btn-color: #e37083;
    --mdb-btn-hover-bg: #42171e;
    --mdb-btn-hover-color: #d1485f;
    --mdb-btn-focus-bg: #42171e;
    --mdb-btn-focus-color: #d1485f;
    --mdb-btn-active-bg: #42171e;
    --mdb-btn-active-color: #c6445a
}

.btn-outline-warning {
    --mdb-btn-bg: transparent;
    --mdb-btn-color: #e4a11b;
    --mdb-btn-hover-bg: #fefaf4;
    --mdb-btn-hover-color: #d9991a;
    --mdb-btn-focus-bg: #fefaf4;
    --mdb-btn-focus-color: #d9991a;
    --mdb-btn-active-bg: #fefaf4;
    --mdb-btn-active-color: #cd9118;
    --mdb-btn-outline-border-color: #e4a11b;
    --mdb-btn-outline-focus-border-color: #b68116;
    --mdb-btn-outline-hover-border-color: #b68116;
    border-color: var(--mdb-btn-outline-border-color)
}

:not(.btn-check)+.btn-outline-warning:hover,
.btn-outline-warning:first-child:hover,
.btn-outline-warning:focus-visible,
.btn-outline-warning:hover {
    border-color: var(--mdb-btn-outline-hover-border-color)
}

.btn-check:focus-visible+.btn-outline-warning,
.btn-check:focus+.btn-outline-warning,
.btn-outline-warning:focus {
    border-color: var(--mdb-btn-outline-focus-border-color)
}

.btn-check:checked+.btn-outline-warning,
.btn-check:active+.btn-outline-warning,
.btn-outline-warning:active,
.btn-outline-warning.active,
.btn-outline-warning.show {
    border-color: var(--mdb-btn-outline-active-border-color)
}

.btn-check:checked+.btn-outline-warning:focus,
.btn-check:active+.btn-outline-warning:focus,
.btn-outline-warning:active:focus,
.btn-outline-warning.active:focus,
.btn-outline-warning.show:focus {
    border-color: var(--mdb-btn-outline-focus-border-color)
}

.btn-outline-warning:disabled,
.btn-outline-warning.disabled,
fieldset:disabled .btn-outline-warning {
    border-color: var(--mdb-btn-outline-border-color)
}

[data-mdb-theme=dark] .btn-outline-warning {
    --mdb-btn-bg: transparent;
    --mdb-btn-color: #e9b449;
    --mdb-btn-hover-bg: #443008;
    --mdb-btn-hover-color: #d9991a;
    --mdb-btn-focus-bg: #443008;
    --mdb-btn-focus-color: #d9991a;
    --mdb-btn-active-bg: #443008;
    --mdb-btn-active-color: #cd9118
}

.btn-outline-info {
    --mdb-btn-bg: transparent;
    --mdb-btn-color: #54b4d3;
    --mdb-btn-hover-bg: #f6fbfd;
    --mdb-btn-hover-color: #50abc8;
    --mdb-btn-focus-bg: #f6fbfd;
    --mdb-btn-focus-color: #50abc8;
    --mdb-btn-active-bg: #f6fbfd;
    --mdb-btn-active-color: #4ca2be;
    --mdb-btn-outline-border-color: #54b4d3;
    --mdb-btn-outline-focus-border-color: #4390a9;
    --mdb-btn-outline-hover-border-color: #4390a9;
    border-color: var(--mdb-btn-outline-border-color)
}

:not(.btn-check)+.btn-outline-info:hover,
.btn-outline-info:first-child:hover,
.btn-outline-info:focus-visible,
.btn-outline-info:hover {
    border-color: var(--mdb-btn-outline-hover-border-color)
}

.btn-check:focus-visible+.btn-outline-info,
.btn-check:focus+.btn-outline-info,
.btn-outline-info:focus {
    border-color: var(--mdb-btn-outline-focus-border-color)
}

.btn-check:checked+.btn-outline-info,
.btn-check:active+.btn-outline-info,
.btn-outline-info:active,
.btn-outline-info.active,
.btn-outline-info.show {
    border-color: var(--mdb-btn-outline-active-border-color)
}

.btn-check:checked+.btn-outline-info:focus,
.btn-check:active+.btn-outline-info:focus,
.btn-outline-info:active:focus,
.btn-outline-info.active:focus,
.btn-outline-info.show:focus {
    border-color: var(--mdb-btn-outline-focus-border-color)
}

.btn-outline-info:disabled,
.btn-outline-info.disabled,
fieldset:disabled .btn-outline-info {
    border-color: var(--mdb-btn-outline-border-color)
}

[data-mdb-theme=dark] .btn-outline-info {
    --mdb-btn-bg: transparent;
    --mdb-btn-color: #76c3dc;
    --mdb-btn-hover-bg: #19363f;
    --mdb-btn-hover-color: #50abc8;
    --mdb-btn-focus-bg: #19363f;
    --mdb-btn-focus-color: #50abc8;
    --mdb-btn-active-bg: #19363f;
    --mdb-btn-active-color: #4ca2be
}

.btn-outline-light {
    --mdb-btn-bg: transparent;
    --mdb-btn-color: #fbfbfb;
    --mdb-btn-hover-bg: white;
    --mdb-btn-hover-color: #eeeeee;
    --mdb-btn-focus-bg: white;
    --mdb-btn-focus-color: #eeeeee;
    --mdb-btn-active-bg: white;
    --mdb-btn-active-color: #e2e2e2;
    --mdb-btn-outline-border-color: #fbfbfb;
    --mdb-btn-outline-focus-border-color: #c9c9c9;
    --mdb-btn-outline-hover-border-color: #c9c9c9;
    border-color: var(--mdb-btn-outline-border-color)
}

:not(.btn-check)+.btn-outline-light:hover,
.btn-outline-light:first-child:hover,
.btn-outline-light:focus-visible,
.btn-outline-light:hover {
    border-color: var(--mdb-btn-outline-hover-border-color)
}

.btn-check:focus-visible+.btn-outline-light,
.btn-check:focus+.btn-outline-light,
.btn-outline-light:focus {
    border-color: var(--mdb-btn-outline-focus-border-color)
}

.btn-check:checked+.btn-outline-light,
.btn-check:active+.btn-outline-light,
.btn-outline-light:active,
.btn-outline-light.active,
.btn-outline-light.show {
    border-color: var(--mdb-btn-outline-active-border-color)
}

.btn-check:checked+.btn-outline-light:focus,
.btn-check:active+.btn-outline-light:focus,
.btn-outline-light:active:focus,
.btn-outline-light.active:focus,
.btn-outline-light.show:focus {
    border-color: var(--mdb-btn-outline-focus-border-color)
}

.btn-outline-light:disabled,
.btn-outline-light.disabled,
fieldset:disabled .btn-outline-light {
    border-color: var(--mdb-btn-outline-border-color)
}

[data-mdb-theme=dark] .btn-outline-light {
    --mdb-btn-bg: transparent;
    --mdb-btn-color: #fcfcfc;
    --mdb-btn-hover-bg: #4b4b4b;
    --mdb-btn-hover-color: #eeeeee;
    --mdb-btn-focus-bg: #4b4b4b;
    --mdb-btn-focus-color: #eeeeee;
    --mdb-btn-active-bg: #4b4b4b;
    --mdb-btn-active-color: #e2e2e2
}

.btn-outline-dark {
    --mdb-btn-bg: transparent;
    --mdb-btn-color: #332d2d;
    --mdb-btn-hover-bg: whitesmoke;
    --mdb-btn-hover-color: #302b2b;
    --mdb-btn-focus-bg: whitesmoke;
    --mdb-btn-focus-color: #302b2b;
    --mdb-btn-active-bg: whitesmoke;
    --mdb-btn-active-color: #2e2929;
    --mdb-btn-outline-border-color: #332d2d;
    --mdb-btn-outline-focus-border-color: #292424;
    --mdb-btn-outline-hover-border-color: #292424;
    border-color: var(--mdb-btn-outline-border-color)
}

:not(.btn-check)+.btn-outline-dark:hover,
.btn-outline-dark:first-child:hover,
.btn-outline-dark:focus-visible,
.btn-outline-dark:hover {
    border-color: var(--mdb-btn-outline-hover-border-color)
}

.btn-check:focus-visible+.btn-outline-dark,
.btn-check:focus+.btn-outline-dark,
.btn-outline-dark:focus {
    border-color: var(--mdb-btn-outline-focus-border-color)
}

.btn-check:checked+.btn-outline-dark,
.btn-check:active+.btn-outline-dark,
.btn-outline-dark:active,
.btn-outline-dark.active,
.btn-outline-dark.show {
    border-color: var(--mdb-btn-outline-active-border-color)
}

.btn-check:checked+.btn-outline-dark:focus,
.btn-check:active+.btn-outline-dark:focus,
.btn-outline-dark:active:focus,
.btn-outline-dark.active:focus,
.btn-outline-dark.show:focus {
    border-color: var(--mdb-btn-outline-focus-border-color)
}

.btn-outline-dark:disabled,
.btn-outline-dark.disabled,
fieldset:disabled .btn-outline-dark {
    border-color: var(--mdb-btn-outline-border-color)
}

[data-mdb-theme=dark] .btn-outline-dark {
    --mdb-btn-bg: transparent;
    --mdb-btn-color: #5c5757;
    --mdb-btn-hover-bg: #0f0e0e;
    --mdb-btn-hover-color: #302b2b;
    --mdb-btn-focus-bg: #0f0e0e;
    --mdb-btn-focus-color: #302b2b;
    --mdb-btn-active-bg: #0f0e0e;
    --mdb-btn-active-color: #2e2929
}

.btn-link {
    --mdb-btn-font-weight: 500;
    --mdb-btn-color: #3b71ca;
    --mdb-btn-hover-color: #386bc0;
    --mdb-btn-hover-bg: hsl(0, 0%, 96%);
    --mdb-btn-focus-color: #3566b6;
    --mdb-btn-active-color: #3260ac;
    --mdb-btn-disabled-color: #9e9e9e;
    --mdb-btn-box-shadow: none;
    text-decoration: none;
    box-shadow: var(--mdb-btn-box-shadow)
}

:not(.btn-check)+.btn-link:hover,
.btn-link:first-child:hover,
.btn-link:focus-visible,
.btn-link:hover {
    text-decoration: none;
    box-shadow: var(--mdb-btn-box-shadow)
}

.btn-check:focus-visible+.btn-link,
.btn-check:focus+.btn-link,
.btn-link:focus {
    color: var(--mdb-btn-focus-color);
    box-shadow: var(--mdb-btn-box-shadow)
}

.btn-check:checked+.btn-link,
.btn-check:active+.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link.show {
    color: var(--mdb-btn-active-color);
    box-shadow: var(--mdb-btn-box-shadow)
}

.btn-check:checked+.btn-link:focus,
.btn-check:active+.btn-link:focus,
.btn-link:active:focus,
.btn-link.active:focus,
.btn-link.show:focus {
    color: var(--mdb-btn-focus-color);
    box-shadow: var(--mdb-btn-box-shadow)
}

.btn-link:disabled,
.btn-link.disabled,
fieldset:disabled .btn-link {
    box-shadow: var(--mdb-btn-box-shadow)
}

.btn-tertiary {
    --mdb-btn-font-weight: 500;
    --mdb-btn-color: #3b71ca;
    --mdb-btn-hover-color: #386bc0;
    --mdb-btn-hover-bg: transparent;
    --mdb-btn-focus-color: #3566b6;
    --mdb-btn-active-color: #3260ac;
    --mdb-btn-disabled-color: #9e9e9e;
    --mdb-btn-box-shadow: none;
    padding-left: 0px;
    padding-right: 0px;
    text-decoration: none;
    box-shadow: var(--mdb-btn-box-shadow)
}

:not(.btn-check)+.btn-tertiary:hover,
.btn-tertiary:first-child:hover,
.btn-tertiary:focus-visible,
.btn-tertiary:hover {
    text-decoration: none;
    box-shadow: var(--mdb-btn-box-shadow)
}

.btn-check:focus-visible+.btn-tertiary,
.btn-check:focus+.btn-tertiary,
.btn-tertiary:focus {
    color: var(--mdb-btn-focus-color);
    box-shadow: var(--mdb-btn-box-shadow)
}

.btn-check:checked+.btn-tertiary,
.btn-check:active+.btn-tertiary,
.btn-tertiary:active,
.btn-tertiary.active,
.btn-tertiary.show {
    color: var(--mdb-btn-active-color);
    box-shadow: var(--mdb-btn-box-shadow)
}

.btn-check:checked+.btn-tertiary:focus,
.btn-check:active+.btn-tertiary:focus,
.btn-tertiary:active:focus,
.btn-tertiary.active:focus,
.btn-tertiary.show:focus {
    color: var(--mdb-btn-focus-color);
    box-shadow: var(--mdb-btn-box-shadow)
}

.btn-tertiary:disabled,
.btn-tertiary.disabled,
fieldset:disabled .btn-tertiary {
    box-shadow: var(--mdb-btn-box-shadow)
}

[data-mdb-theme=dark] .btn-secondary {
    --mdb-btn-bg: #b1c6ea;
    --mdb-btn-hover-bg: #9db8e5;
    --mdb-btn-focus-bg: #9db8e5;
    --mdb-btn-active-bg: #9db8e5
}

[data-mdb-theme=dark] .btn-link {
    --mdb-btn-color: #9fa6b2;
    --mdb-btn-hover-color: #bcc1c9;
    --mdb-btn-hover-bg: #404247;
    --mdb-btn-focus-color: #bcc1c9;
    --mdb-btn-active-color: #bcc1c9
}

[data-mdb-theme=dark] .btn-tertiary {
    --mdb-btn-color: #9fa6b2;
    --mdb-btn-hover-color: #bcc1c9;
    --mdb-btn-focus-color: #bcc1c9;
    --mdb-btn-active-color: #bcc1c9
}

.btn-lg,
.btn-group-lg>.btn {
    --mdb-btn-padding-top: 0.75rem;
    --mdb-btn-padding-bottom: 0.6875rem;
    --mdb-btn-padding-x: 1.6875rem;
    --mdb-btn-font-size: 0.875rem;
    --mdb-btn-line-height: 1.6
}

.btn-sm,
.btn-group-sm>.btn {
    --mdb-btn-padding-top: 0.375rem;
    --mdb-btn-padding-bottom: 0.3125rem;
    --mdb-btn-padding-x: 1rem;
    --mdb-btn-font-size: 0.75rem;
    --mdb-btn-line-height: 1.5
}

.btn-rounded {
    --mdb-btn-border-radius: 10rem;
    border-radius: var(--mdb-btn-border-radius)
}

.btn-floating,
[class*=btn-outline-].btn-floating {
    --mdb-btn-border-radius: 50%;
    border-radius: var(--mdb-btn-border-radius);
    padding: 0;
    position: relative;
    display: inline-flex;
    align-items: center;
    justify-content: center
}

.btn-floating {
    --mdb-btn-width: 2.3125rem;
    --mdb-btn-height: 2.3125rem;
    --mdb-btn-icon-width: 2.3125rem;
    --mdb-btn-icon-line-height: 2.3125rem;
    --mdb-btn-width-lg: 2.8125rem;
    --mdb-btn-height-lg: 2.8125rem;
    --mdb-btn-icon-width-lg: 2.8125rem;
    --mdb-btn-icon-line-height-lg: 2.8125rem;
    --mdb-btn-width-sm: 1.8125rem;
    --mdb-btn-height-sm: 1.8125rem;
    --mdb-btn-icon-width-sm: 1.8125rem;
    --mdb-btn-icon-line-height-sm: 1.8125rem;
    width: var(--mdb-btn-width);
    height: var(--mdb-btn-height)
}

.btn-floating .fas,
.btn-floating .far,
.btn-floating .fab {
    width: var(--mdb-btn-icon-width);
    line-height: var(--mdb-btn-icon-line-height)
}

.btn-floating.btn-lg,
.btn-group-lg>.btn-floating.btn {
    width: var(--mdb-btn-width-lg);
    height: var(--mdb-btn-height-lg)
}

.btn-floating.btn-lg .fas,
.btn-group-lg>.btn-floating.btn .fas,
.btn-floating.btn-lg .far,
.btn-group-lg>.btn-floating.btn .far,
.btn-floating.btn-lg .fab,
.btn-group-lg>.btn-floating.btn .fab {
    width: var(--mdb-btn-icon-width-lg);
    line-height: var(--mdb-btn-icon-line-height-lg)
}

.btn-floating.btn-sm,
.btn-group-sm>.btn-floating.btn {
    width: var(--mdb-btn-width-sm);
    height: var(--mdb-btn-height-sm)
}

.btn-floating.btn-sm .fas,
.btn-group-sm>.btn-floating.btn .fas,
.btn-floating.btn-sm .far,
.btn-group-sm>.btn-floating.btn .far,
.btn-floating.btn-sm .fab,
.btn-group-sm>.btn-floating.btn .fab {
    width: var(--mdb-btn-icon-width-sm);
    line-height: var(--mdb-btn-icon-line-height-sm)
}

[class*=btn-outline-].btn-floating {
    --mdb-btn-icon-width: 2.0625rem;
    --mdb-btn-icon-width-lg: 2.5625rem;
    --mdb-btn-icon-width-sm: 1.5625rem;
    --mdb-btn-icon-line-height: 2.0625rem;
    --mdb-btn-icon-line-height-lg: 2.5625rem;
    --mdb-btn-icon-line-height-sm: 1.5625rem
}

[class*=btn-outline-].btn-floating .fas,
[class*=btn-outline-].btn-floating .far,
[class*=btn-outline-].btn-floating .fab {
    width: var(--mdb-btn-icon-width);
    line-height: var(--mdb-btn-icon-line-height)
}

[class*=btn-outline-].btn-floating.btn-lg .fas,
.btn-group-lg>[class*=btn-outline-].btn-floating.btn .fas,
[class*=btn-outline-].btn-floating.btn-lg .far,
.btn-group-lg>[class*=btn-outline-].btn-floating.btn .far,
[class*=btn-outline-].btn-floating.btn-lg .fab,
.btn-group-lg>[class*=btn-outline-].btn-floating.btn .fab {
    width: var(--mdb-btn-icon-width-lg);
    line-height: var(--mdb-btn-icon-line-height-lg)
}

[class*=btn-outline-].btn-floating.btn-sm .fas,
.btn-group-sm>[class*=btn-outline-].btn-floating.btn .fas,
[class*=btn-outline-].btn-floating.btn-sm .far,
.btn-group-sm>[class*=btn-outline-].btn-floating.btn .far,
[class*=btn-outline-].btn-floating.btn-sm .fab,
.btn-group-sm>[class*=btn-outline-].btn-floating.btn .fab {
    width: var(--mdb-btn-icon-width-sm);
    line-height: var(--mdb-btn-icon-line-height-sm)
}

.fixed-action-btn {
    --mdb-btn-right: 2.1875rem;
    --mdb-btn-bottom: 2.1875rem;
    --mdb-btn-zindex: 1030;
    --mdb-btn-padding-top: 0.9375rem;
    --mdb-btn-padding-bottom: 1.25rem;
    --mdb-btn-padding-x: 1.25rem;
    --mdb-btn-margin-bottom: 1.5rem;
    position: fixed;
    right: var(--mdb-btn-right);
    bottom: var(--mdb-btn-bottom);
    z-index: var(--mdb-btn-zindex);
    display: flex;
    flex-flow: column-reverse nowrap;
    align-items: center;
    padding: var(--mdb-btn-padding-top) var(--mdb-btn-padding-x) var(--mdb-btn-padding-bottom);
    margin-bottom: 0;
    height: auto;
    overflow: hidden
}

.fixed-action-btn>.btn-floating {
    position: relative;
    transform: scale(1.2);
    z-index: 10
}

.fixed-action-btn ul {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    display: flex;
    flex-direction: column;
    padding: 0;
    margin: 0;
    margin-bottom: 0;
    text-align: center;
    opacity: 0;
    transition: transform .4s, opacity .4s;
    z-index: -1
}

.fixed-action-btn ul li {
    z-index: 0;
    display: flex;
    margin-right: auto;
    margin-bottom: var(--mdb-btn-margin-bottom);
    margin-left: auto
}

.fixed-action-btn ul li:first-of-type {
    margin-top: calc(var(--mdb-btn-margin-bottom)*.5)
}

.fixed-action-btn ul a.btn {
    opacity: 0;
    transition: opacity .4s ease-in
}

.fixed-action-btn ul a.btn.shown {
    opacity: 1
}

.fixed-action-btn.active ul {
    opacity: 1
}

.btn-block {
    --mdb-btn-margin-top: 0.5rem;
    display: block;
    width: 100%
}

.btn-block+.btn-block {
    margin-top: var(--mdb-btn-margin-top)
}

hr.divider-horizontal:not([size]) {
    height: 2px
}

.divider-horizontal {
    opacity: 1;
    background-color: #f5f5f5;
    height: 2px
}

.divider-vertical {
    opacity: 1;
    background-color: #f5f5f5;
    display: inline-block;
    width: 2px;
    margin: 0 1rem
}

hr.divider-horizontal-blurry {
    background-image: linear-gradient(90deg, transparent, hsl(0, 0%, 40%), transparent);
    background-color: rgba(0, 0, 0, 0)
}

hr.divider-vertical-blurry {
    background-image: linear-gradient(180deg, transparent, hsl(0, 0%, 40%), transparent);
    background-color: rgba(0, 0, 0, 0);
    width: 1px;
    top: 0;
    right: 0
}

.dropdown-menu {
    --mdb-dropdown-item-border-radius: 0.5rem;
    color: var(--mdb-dropdown-color);
    margin: 0;
    padding-top: 0;
    padding-bottom: 0;
    border: 0;
    box-shadow: var(--mdb-dropdown-box-shadow);
    font-size: var(--mdb-dropdown-font-size);
    top: 100%;
    left: 0;
    margin-top: var(--mdb-dropdown-spacer)
}

.dropdown-menu>li {
    border-radius: 0
}

.dropdown-menu>li:first-child {
    border-top-left-radius: var(--mdb-dropdown-item-border-radius);
    border-top-right-radius: var(--mdb-dropdown-item-border-radius);
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0
}

.dropdown-menu>li:first-child .dropdown-item {
    border-top-left-radius: var(--mdb-dropdown-item-border-radius);
    border-top-right-radius: var(--mdb-dropdown-item-border-radius);
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0
}

.dropdown-menu>li:not(:first-child):not(:last-child) .dropdown-item {
    border-radius: 0
}

.dropdown-menu>li:last-child {
    border-top-left-radius: 0;
    border-top-right-radius: 0;
    border-bottom-left-radius: var(--mdb-dropdown-item-border-radius);
    border-bottom-right-radius: var(--mdb-dropdown-item-border-radius)
}

.dropdown-menu>li:last-child .dropdown-item {
    border-top-left-radius: 0;
    border-top-right-radius: 0;
    border-bottom-left-radius: var(--mdb-dropdown-item-border-radius);
    border-bottom-right-radius: var(--mdb-dropdown-item-border-radius)
}

.dropdown-menu.animation {
    --mdb-dropdown-menu-animated-animation-duration: 0.55s;
    --mdb-dropdown-menu-animated-animation-timing-function: ease;
    display: block;
    animation-duration: var(--mdb-dropdown-menu-animated-animation-duration);
    animation-timing-function: var(--mdb-dropdown-menu-animated-animation-timing-function)
}

.dropdown-item {
    --mdb-dropdown-state-color: var(--mdb-surface-color);
    --mdb-dropdown-state-background-color: var(--mdb-highlight-bg-color);
    padding: var(--mdb-dropdown-item-padding-y) var(--mdb-dropdown-item-padding-x);
    color: var(--mdb-dropdown-color);
    border-radius: 0
}

.dropdown-item:hover,
.dropdown-item:focus {
    color: var(--mdb-dropdown-state-color);
    background-color: var(--mdb-dropdown-state-background-color)
}

.dropdown-item.active,
.dropdown-item:active {
    color: var(--mdb-dropdown-state-color);
    background-color: var(--mdb-dropdown-state-background-color)
}

.dropdown-item:focus {
    outline: none
}

.hidden-arrow.dropdown-toggle:after {
    display: none
}

.animation {
    animation-duration: 1s;
    animation-fill-mode: both;
    padding: auto
}

@media(prefers-reduced-motion) {
    .animation {
        transition: none !important;
        animation: unset !important
    }
}

@keyframes fade-in {
    from {
        opacity: 0
    }

    to {
        opacity: 1
    }
}

.fade-in {
    animation-name: fade-in
}

@keyframes fade-out {
    from {
        opacity: 1
    }

    to {
        opacity: 0
    }
}

.fade-out {
    animation-name: fade-out
}

.dropdown-divider {
    --mdb-dropdown-divider-border-top-width: 2px;
    --mdb-dropdown-divider-border-top-bg: var(--mdb-divider-color);
    border-top: var(--mdb-dropdown-divider-border-top-width) solid var(--mdb-dropdown-divider-border-top-bg);
    opacity: 1
}

.dropdown-menu INPUT:not(:-webkit-autofill),
.dropdown-menu SELECT:not(:-webkit-autofill),
.dropdown-menu TEXTAREA:not(:-webkit-autofill) {
    animation-name: none !important
}

.btn-group,
.btn-group-vertical {
    --mdb-btn-box-shadow: 0 4px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.35);
    --mdb-btn-hover-box-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-focus-box-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-active-box-shadow: 0 8px 9px -4px rgba(var(--mdb-box-shadow-color-rgb), 0.15), 0 4px 18px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.1);
    --mdb-btn-group-transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    box-shadow: var(--mdb-btn-box-shadow);
    transition: var(--mdb-btn-group-transition)
}

.btn-group:hover,
.btn-group-vertical:hover {
    box-shadow: var(--mdb-btn-hover-box-shadow)
}

.btn-group:focus,
.btn-group.focus,
.btn-group-vertical:focus,
.btn-group-vertical.focus {
    box-shadow: var(--mdb-btn-focus-box-shadow)
}

.btn-group:active,
.btn-group.active,
.btn-group-vertical:active,
.btn-group-vertical.active {
    box-shadow: var(--mdb-btn-active-box-shadow)
}

.btn-group:active:focus,
.btn-group.active:focus,
.btn-group-vertical:active:focus,
.btn-group-vertical.active:focus {
    box-shadow: var(--mdb-btn-focus-box-shadow)
}

.btn-group:disabled,
.btn-group.disabled,
fieldset:disabled .btn-group,
.btn-group-vertical:disabled,
.btn-group-vertical.disabled,
fieldset:disabled .btn-group-vertical {
    box-shadow: var(--mdb-btn-box-shadow);
    border: 0
}

.btn-group>.btn,
.btn-group-vertical>.btn {
    box-shadow: none
}

:not(.btn-check)+.btn-group>.btn:hover,
.btn-group>.btn:first-child:hover,
.btn-group>.btn:focus-visible,
.btn-group>.btn:hover,
:not(.btn-check)+.btn-group-vertical>.btn:hover,
.btn-group-vertical>.btn:first-child:hover,
.btn-group-vertical>.btn:focus-visible,
.btn-group-vertical>.btn:hover {
    box-shadow: none !important
}

.btn-check:focus-visible+.btn-group>.btn,
.btn-check:focus+.btn-group>.btn,
.btn-group>.btn:focus,
.btn-check:focus-visible+.btn-group-vertical>.btn,
.btn-check:focus+.btn-group-vertical>.btn,
.btn-group-vertical>.btn:focus {
    box-shadow: none
}

.btn-check:checked+.btn-group>.btn,
.btn-check:active+.btn-group>.btn,
.btn-group>.btn:active,
.btn-group>.btn.active,
.btn-group>.btn.show,
.btn-check:checked+.btn-group-vertical>.btn,
.btn-check:active+.btn-group-vertical>.btn,
.btn-group-vertical>.btn:active,
.btn-group-vertical>.btn.active,
.btn-group-vertical>.btn.show {
    box-shadow: none
}

.btn-check:checked+.btn-group>.btn:focus,
.btn-check:active+.btn-group>.btn:focus,
.btn-group>.btn:active:focus,
.btn-group>.btn.active:focus,
.btn-group>.btn.show:focus,
.btn-check:checked+.btn-group-vertical>.btn:focus,
.btn-check:active+.btn-group-vertical>.btn:focus,
.btn-group-vertical>.btn:active:focus,
.btn-group-vertical>.btn.active:focus,
.btn-group-vertical>.btn.show:focus {
    box-shadow: none
}

.btn-group>.btn:disabled,
.btn-group>.btn.disabled,
fieldset:disabled .btn-group>.btn,
.btn-group-vertical>.btn:disabled,
.btn-group-vertical>.btn.disabled,
fieldset:disabled .btn-group-vertical>.btn {
    box-shadow: none
}

.btn-group>.btn-group,
.btn-group-vertical>.btn-group {
    box-shadow: none
}

.btn-group>.btn-link:first-child,
.btn-group>.btn-tertiary:first-child,
.btn-group-vertical>.btn-link:first-child,
.btn-group-vertical>.btn-tertiary:first-child {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0
}

.btn-group>.btn-link:last-child,
.btn-group>.btn-tertiary:last-child,
.btn-group-vertical>.btn-link:last-child,
.btn-group-vertical>.btn-tertiary:last-child {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0
}

.btn-group,
.btn-group-lg>.btn,
.btn-group-sm>.btn {
    --mdb-btn-border-radius: 0.25rem;
    border-radius: var(--mdb-btn-border-radius)
}

.nav-tabs {
    border-bottom: 0
}

.nav-tabs .nav-link {
    --mdb-nav-tabs-link-font-weight: 500;
    --mdb-nav-tabs-link-font-size: 12px;
    --mdb-nav-tabs-link-color: rgba(var(--mdb-emphasis-color-rgb), 0.55);
    --mdb-nav-tabs-link-padding-top: 17px;
    --mdb-nav-tabs-link-padding-bottom: 16px;
    --mdb-nav-tabs-link-padding-x: 29px;
    --mdb-nav-tabs-link-hover-bgc: var(--mdb-highlight-bg-color);
    --mdb-nav-tabs-link-border-bottom-width: 2px;
    --mdb-nav-tabs-link-active-color: #3b71ca;
    --mdb-nav-tabs-link-active-border-color: #3b71ca;
    border-width: 0;
    border-bottom: var(--mdb-nav-tabs-link-border-bottom-width) solid rgba(0, 0, 0, 0);
    border-radius: 0;
    text-transform: uppercase;
    line-height: 1;
    font-weight: var(--mdb-nav-tabs-link-font-weight);
    font-size: var(--mdb-nav-tabs-link-font-size);
    color: var(--mdb-nav-tabs-link-color);
    padding: var(--mdb-nav-tabs-link-padding-top) var(--mdb-nav-tabs-link-padding-x) var(--mdb-nav-tabs-link-padding-bottom) var(--mdb-nav-tabs-link-padding-x)
}

.nav-tabs .nav-link:hover {
    background-color: var(--mdb-nav-tabs-link-hover-bgc);
    border-color: rgba(0, 0, 0, 0)
}

.nav-tabs .nav-link:focus {
    border-color: rgba(0, 0, 0, 0)
}

.nav-tabs .nav-link.active,
.nav-tabs .nav-item.show .nav-link {
    color: var(--mdb-nav-tabs-link-active-color);
    border-color: var(--mdb-nav-tabs-link-active-border-color)
}

.nav-pills {
    margin-left: -0.5rem
}

.nav-pills .nav-link {
    --mdb-nav-pills-link-border-radius: 0.25rem;
    --mdb-nav-pills-link-font-size: 12px;
    --mdb-nav-pills-link-padding-top: 17px;
    --mdb-nav-pills-link-padding-bottom: 16px;
    --mdb-nav-pills-link-padding-x: 29px;
    --mdb-nav-pills-link-line-height: 1;
    --mdb-nav-pills-link-hover-bg: var(--mdb-highlight-bg-color);
    --mdb-nav-pills-link-font-weight: 500;
    --mdb-nav-pills-link-color: rgba(var(--mdb-emphasis-color-rgb), 0.55);
    --mdb-nav-pills-margin: 0.5rem;
    border-radius: var(--mdb-nav-pills-link-border-radius);
    font-size: var(--mdb-nav-pills-link-font-size);
    text-transform: uppercase;
    padding: var(--mdb-nav-pills-link-padding-top) var(--mdb-nav-pills-link-padding-x) var(--mdb-nav-pills-link-padding-bottom) var(--mdb-nav-pills-link-padding-x);
    line-height: var(--mdb-nav-pills-link-line-height);
    background-color: var(--mdb-nav-pills-link-hover-bg);
    font-weight: var(--mdb-nav-pills-link-font-weight);
    color: var(--mdb-nav-pills-link-color);
    margin: var(--mdb-nav-pills-margin)
}

.nav-pills .nav-link.active,
.nav-pills .show>.nav-link {
    --mdb-nav-pills-link-active-bg: var(--mdb-primary-bg-subtle);
    --mdb-nav-pills-link-active-color: var(--mdb-primary-text-emphasis);
    background-color: var(--mdb-nav-pills-link-active-bg);
    color: var(--mdb-nav-pills-link-active-color)
}

.nav-fill .nav-item .nav-link,
.nav-justified .nav-item .nav-link {
    width: auto
}

.navbar {
    --mdb-navbar-box-shadow: 0 4px 12px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.07), 0 2px 4px rgba(var(--mdb-box-shadow-color-rgb), 0.05);
    --mdb-navbar-padding-top: 0.5625rem;
    --mdb-navbar-brand-img-margin-right: 0.25rem;
    box-shadow: var(--mdb-navbar-box-shadow);
    padding-top: var(--mdb-navbar-padding-top)
}

.navbar-toggler {
    border: 0
}

.navbar-toggler:focus {
    box-shadow: none
}

.navbar-dark .navbar-toggler,
.navbar-light .navbar-toggler {
    border: 0
}

.navbar-brand {
    display: flex;
    align-items: center
}

.navbar-brand img {
    margin-right: var(--mdb-navbar-brand-img-margin-right)
}

.navbar-nav .dropdown-menu {
    position: absolute
}

.navbar-light .navbar-toggler-icon {
    background-image: none
}

.navbar-dark .navbar-toggler-icon {
    background-image: none
}

.navbar-dark,
.navbar[data-mdb-theme=dark] {
    --mdb-navbar-color: rgba(255, 255, 255, 0.55);
    --mdb-navbar-hover-color: rgba(255, 255, 255, 0.75);
    --mdb-navbar-disabled-color: rgba(255, 255, 255, 0.25);
    --mdb-navbar-active-color: #fff;
    --mdb-navbar-brand-color: #fff;
    --mdb-navbar-brand-hover-color: #fff;
    --mdb-navbar-toggler-border-color: rgba(255, 255, 255, 0.1);
    --mdb-navbar-toggler-icon-bg: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%28255, 255, 255, 0.55%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e")
}

.card {
    border: 0
}

.card .bg-image {
    border-top-left-radius: var(--mdb-card-border-radius);
    border-top-right-radius: var(--mdb-card-border-radius)
}

.card[class*=bg-] .card-header {
    --mdb-card-header-border-bottom-color: rgba(0, 0, 0, 0.175);
    border-bottom-color: var(--mdb-card-header-border-bottom-color)
}

.card[class*=bg-] .card-footer {
    --mdb-card-footer-border-top-color: rgba(0, 0, 0, 0.175);
    border-top-color: var(--mdb-card-footer-border-top-color)
}

.card-header {
    --mdb-card-header-border-width: 2px;
    --mdb-card-header-border-color: var(--mdb-divider-color);
    border-bottom: var(--mdb-card-header-border-width) solid var(--mdb-card-header-border-color)
}

.card-body[class*=bg-] {
    border-bottom-left-radius: var(--mdb-card-border-radius);
    border-bottom-right-radius: var(--mdb-card-border-radius)
}

.card-footer {
    --mdb-card-footer-border-color: var(--mdb-divider-color);
    --mdb-card-footer-border-width: 2px;
    border-top: var(--mdb-card-footer-border-width) solid var(--mdb-card-footer-border-color)
}

.card-img-left {
    border-top-left-radius: var(--mdb-card-border-radius);
    border-bottom-left-radius: var(--mdb-card-border-radius)
}

.navbar .breadcrumb {
    --mdb-breadcrumb-item-color: rgba(var(--mdb-emphasis-color-rgb), 0.55);
    --mdb-breadcrumb-item-hover-color: rgba(var(--mdb-emphasis-color-rgb), 0.7);
    --mdb-breadcrumb-item-before-color: rgba(var(--mdb-emphasis-color-rgb), 0.55);
    --mdb-breadcrumb-item-transition: color 0.15s ease-in-out;
    background-color: rgba(0, 0, 0, 0);
    margin-bottom: 0
}

.navbar .breadcrumb .breadcrumb-item a {
    color: var(--mdb-breadcrumb-item-color);
    transition: var(--mdb-breadcrumb-item-transition)
}

.navbar .breadcrumb .breadcrumb-item a:hover,
.navbar .breadcrumb .breadcrumb-item a:focus {
    color: var(--mdb-breadcrumb-item-hover-color)
}

.navbar .breadcrumb .breadcrumb-item+.breadcrumb-item:before {
    color: var(--mdb-breadcrumb-item-before-color)
}

.pagination {
    --mdb-pagination-border-radius: 0.25rem;
    --mdb-pagination-active-transition: all 0.2s linear;
    --mdb-pagination-active-font-weight: 500;
    --mdb-pagination-circle-border-radius: 50%;
    --mdb-pagination-circle-padding-x: 0.841rem;
    --mdb-pagination-circle-padding-l-lg: 1.399414rem;
    --mdb-pagination-circle-padding-r-lg: 1.399415rem;
    --mdb-pagination-circle-padding-l-sm: 0.696rem;
    --mdb-pagination-circle-padding-r-sm: 0.688rem
}

.page-link {
    background-color: rgba(0, 0, 0, 0);
    border: 0;
    outline: 0;
    border-radius: var(--mdb-pagination-border-radius)
}

.page-link:focus {
    box-shadow: none
}

.page-link.active,
.active>.page-link {
    border: 0;
    transition: var(--mdb-pagination-active-transition);
    font-weight: var(--mdb-pagination-active-font-weight)
}

.page-item:not(:first-child) .page-link {
    margin-left: 0
}

.page-item:first-child .page-link {
    border-top-left-radius: var(--mdb-pagination-border-radius);
    border-bottom-left-radius: var(--mdb-pagination-border-radius)
}

.page-item:last-child .page-link {
    border-top-right-radius: var(--mdb-pagination-border-radius);
    border-bottom-right-radius: var(--mdb-pagination-border-radius)
}

.pagination-circle .page-item:first-child .page-link {
    border-radius: var(--mdb-pagination-circle-border-radius)
}

.pagination-circle .page-item:last-child .page-link {
    border-radius: var(--mdb-pagination-circle-border-radius)
}

.pagination-circle .page-link {
    border-radius: var(--mdb-pagination-circle-border-radius);
    padding-left: var(--mdb-pagination-circle-padding-x);
    padding-right: var(--mdb-pagination-circle-padding-x)
}

.pagination-circle.pagination-lg .page-link {
    padding-left: var(--mdb-pagination-circle-padding-l-lg);
    padding-right: var(--mdb-pagination-circle-padding-r-lg)
}

.pagination-circle.pagination-sm .page-link {
    padding-left: var(--mdb-pagination-circle-padding-l-sm);
    padding-right: var(--mdb-pagination-circle-padding-r-sm)
}

.badge-dot {
    --mdb-badge-border-radius: 4.5px;
    --mdb-badge-height: 9px;
    --mdb-badge-width: 9px;
    --mdb-badge-margin-left: -0.3125rem;
    position: absolute;
    min-width: 0;
    width: var(--mdb-badge-width);
    height: var(--mdb-badge-height);
    border-radius: var(--mdb-badge-border-radius);
    padding: 0;
    margin-left: var(--mdb-badge-margin-left)
}

.badge-dot:empty {
    display: inline-block
}

.badge-notification {
    --mdb-badge-font-size: 0.6rem;
    --mdb-badge-padding-x: 0.45em;
    --mdb-badge-padding-y: 0.2em;
    --mdb-badge-margin-top: -0.1rem;
    --mdb-badge-margin-left: -0.5rem;
    position: absolute;
    font-size: var(--mdb-badge-font-size);
    padding: var(--mdb-badge-padding-y) var(--mdb-badge-padding-x);
    margin-top: var(--mdb-badge-margin-top);
    margin-left: var(--mdb-badge-margin-left)
}

.badge-primary {
    background-color: var(--mdb-primary-bg-subtle);
    color: var(--mdb-primary-text-emphasis)
}

.badge-primary i {
    color: var(--mdb-primary-text-emphasis)
}

.badge-secondary {
    background-color: var(--mdb-secondary-bg-subtle);
    color: var(--mdb-secondary-text-emphasis)
}

.badge-secondary i {
    color: var(--mdb-secondary-text-emphasis)
}

.badge-success {
    background-color: var(--mdb-success-bg-subtle);
    color: var(--mdb-success-text-emphasis)
}

.badge-success i {
    color: var(--mdb-success-text-emphasis)
}

.badge-danger {
    background-color: var(--mdb-danger-bg-subtle);
    color: var(--mdb-danger-text-emphasis)
}

.badge-danger i {
    color: var(--mdb-danger-text-emphasis)
}

.badge-warning {
    background-color: var(--mdb-warning-bg-subtle);
    color: var(--mdb-warning-text-emphasis)
}

.badge-warning i {
    color: var(--mdb-warning-text-emphasis)
}

.badge-info {
    background-color: var(--mdb-info-bg-subtle);
    color: var(--mdb-info-text-emphasis)
}

.badge-info i {
    color: var(--mdb-info-text-emphasis)
}

.badge-light {
    background-color: var(--mdb-light-bg-subtle);
    color: var(--mdb-light-text-emphasis)
}

.badge-light i {
    color: var(--mdb-light-text-emphasis)
}

.badge-dark {
    background-color: var(--mdb-dark-bg-subtle);
    color: var(--mdb-dark-text-emphasis)
}

.badge-dark i {
    color: var(--mdb-dark-text-emphasis)
}

.alert {
    border: 0
}

.alert-absolute {
    position: absolute
}

.alert-fixed {
    --mdb-alert-fixed-z-index: 1070;
    position: fixed;
    z-index: var(--mdb-alert-fixed-z-index)
}

.parent-alert-relative {
    position: relative
}

.alert-primary {
    background-color: var(--mdb-primary-bg-subtle);
    color: var(--mdb-primary-text-emphasis)
}

.alert-primary i {
    color: var(--mdb-primary-text-emphasis)
}

.alert-primary .alert-link {
    color: var(--mdb-primary-text-emphasis)
}

.alert-primary .alert-link:hover {
    color: rgba(var(--mdb-primary-text-emphasis), var(--mdb-text-hover-opacity))
}

.alert-secondary {
    background-color: var(--mdb-secondary-bg-subtle);
    color: var(--mdb-secondary-text-emphasis)
}

.alert-secondary i {
    color: var(--mdb-secondary-text-emphasis)
}

.alert-secondary .alert-link {
    color: var(--mdb-secondary-text-emphasis)
}

.alert-secondary .alert-link:hover {
    color: rgba(var(--mdb-secondary-text-emphasis), var(--mdb-text-hover-opacity))
}

.alert-success {
    background-color: var(--mdb-success-bg-subtle);
    color: var(--mdb-success-text-emphasis)
}

.alert-success i {
    color: var(--mdb-success-text-emphasis)
}

.alert-success .alert-link {
    color: var(--mdb-success-text-emphasis)
}

.alert-success .alert-link:hover {
    color: rgba(var(--mdb-success-text-emphasis), var(--mdb-text-hover-opacity))
}

.alert-danger {
    background-color: var(--mdb-danger-bg-subtle);
    color: var(--mdb-danger-text-emphasis)
}

.alert-danger i {
    color: var(--mdb-danger-text-emphasis)
}

.alert-danger .alert-link {
    color: var(--mdb-danger-text-emphasis)
}

.alert-danger .alert-link:hover {
    color: rgba(var(--mdb-danger-text-emphasis), var(--mdb-text-hover-opacity))
}

.alert-warning {
    background-color: var(--mdb-warning-bg-subtle);
    color: var(--mdb-warning-text-emphasis)
}

.alert-warning i {
    color: var(--mdb-warning-text-emphasis)
}

.alert-warning .alert-link {
    color: var(--mdb-warning-text-emphasis)
}

.alert-warning .alert-link:hover {
    color: rgba(var(--mdb-warning-text-emphasis), var(--mdb-text-hover-opacity))
}

.alert-info {
    background-color: var(--mdb-info-bg-subtle);
    color: var(--mdb-info-text-emphasis)
}

.alert-info i {
    color: var(--mdb-info-text-emphasis)
}

.alert-info .alert-link {
    color: var(--mdb-info-text-emphasis)
}

.alert-info .alert-link:hover {
    color: rgba(var(--mdb-info-text-emphasis), var(--mdb-text-hover-opacity))
}

.alert-light {
    background-color: var(--mdb-light-bg-subtle);
    color: var(--mdb-light-text-emphasis)
}

.alert-light i {
    color: var(--mdb-light-text-emphasis)
}

.alert-light .alert-link {
    color: var(--mdb-light-text-emphasis)
}

.alert-light .alert-link:hover {
    color: rgba(var(--mdb-light-text-emphasis), var(--mdb-text-hover-opacity))
}

.alert-dark {
    background-color: var(--mdb-dark-bg-subtle);
    color: var(--mdb-dark-text-emphasis)
}

.alert-dark i {
    color: var(--mdb-dark-text-emphasis)
}

.alert-dark .alert-link {
    color: var(--mdb-dark-text-emphasis)
}

.alert-dark .alert-link:hover {
    color: rgba(var(--mdb-dark-text-emphasis), var(--mdb-text-hover-opacity))
}

.progress {
    border-radius: 0;
    box-shadow: none
}

.list-group {
    --mdb-list-group-item-transition-time: 0.5s
}

.list-group-item-action {
    transition: var(--mdb-list-group-item-transition-time)
}

.list-group-item-action:hover {
    transition: var(--mdb-list-group-item-transition-time)
}

.list-group-light {
    --mdb-list-group-light-item-py: 1rem;
    --mdb-list-group-light-item-border: 2px solid var(--mdb-divider-color);
    --mdb-list-group-light-item-border-width: 2px;
    --mdb-list-group-light-active-border-radius: 0.5rem;
    --mdb-list-group-light-active-bg: var(--mdb-primary-bg-subtle);
    --mdb-list-group-light-active-color: var(--mdb-primary-text-emphasis)
}

.list-group-light .list-group-item {
    padding: var(--mdb-list-group-light-item-py) 0;
    border: var(--mdb-list-group-light-item-border)
}

.list-group-light>.list-group-item {
    border-width: 0 0 var(--mdb-list-group-light-item-border-width)
}

.list-group-light>.list-group-item:last-of-type {
    border: none
}

.list-group-light .active {
    border: none;
    border-radius: var(--mdb-list-group-light-active-border-radius);
    background-color: var(--mdb-list-group-light-active-bg);
    color: var(--mdb-list-group-light-active-color)
}

.list-group-light .list-group-item-action:hover {
    border-radius: var(--mdb-list-group-light-active-border-radius)
}

.list-group-light .list-group-item-action:focus {
    border-radius: var(--mdb-list-group-light-active-border-radius)
}

.list-group-small {
    --mdb-list-group-small-item-py: 0.5rem
}

.list-group-small .list-group-item {
    padding: var(--mdb-list-group-small-item-py) 0
}

.list-group-item-primary {
    background-color: var(--mdb-primary-bg-subtle);
    color: var(--mdb-primary-text-emphasis)
}

.list-group-item-primary i {
    color: var(--mdb-primary-link-emphasis)
}

.list-group-item-secondary {
    background-color: var(--mdb-secondary-bg-subtle);
    color: var(--mdb-secondary-text-emphasis)
}

.list-group-item-secondary i {
    color: var(--mdb-secondary-link-emphasis)
}

.list-group-item-success {
    background-color: var(--mdb-success-bg-subtle);
    color: var(--mdb-success-text-emphasis)
}

.list-group-item-success i {
    color: var(--mdb-success-link-emphasis)
}

.list-group-item-danger {
    background-color: var(--mdb-danger-bg-subtle);
    color: var(--mdb-danger-text-emphasis)
}

.list-group-item-danger i {
    color: var(--mdb-danger-link-emphasis)
}

.list-group-item-warning {
    background-color: var(--mdb-warning-bg-subtle);
    color: var(--mdb-warning-text-emphasis)
}

.list-group-item-warning i {
    color: var(--mdb-warning-link-emphasis)
}

.list-group-item-info {
    background-color: var(--mdb-info-bg-subtle);
    color: var(--mdb-info-text-emphasis)
}

.list-group-item-info i {
    color: var(--mdb-info-link-emphasis)
}

.list-group-item-light {
    background-color: var(--mdb-light-bg-subtle);
    color: var(--mdb-light-text-emphasis)
}

.list-group-item-light i {
    color: var(--mdb-light-link-emphasis)
}

.list-group-item-dark {
    background-color: var(--mdb-dark-bg-subtle);
    color: var(--mdb-dark-text-emphasis)
}

.list-group-item-dark i {
    color: var(--mdb-dark-link-emphasis)
}

.btn-close:focus {
    box-shadow: none
}

.modal-content {
    --mdb-modal-box-shadow: 0 2px 15px -3px rgba(var(--mdb-box-shadow-color-rgb), 0.07), 0 10px 20px -2px rgba(var(--mdb-box-shadow-color-rgb), 0.04);
    border: 0;
    box-shadow: var(--mdb-modal-box-shadow)
}

.toast {
    --mdb-toast-border-bottom-width: 2px;
    --mdb-toast-btn-close-width: 1.3em;
    --mdb-toast-btn-close-mr: -0.375rem;
    --mdb-toast-btn-close-ml: 0.75rem;
    --mdb-toast-bg: var(--mdb-surface-bg);
    --mdb-toast-header-bg: var(--mdb-surface-bg);
    border: 0
}

.toast .btn-close {
    width: var(--mdb-toast-btn-close-width)
}

.toast-header {
    border-bottom-width: var(--mdb-toast-border-bottom-width)
}

.toast-header .btn-close {
    margin-right: var(--mdb-toast-btn-close-mr);
    margin-left: var(--mdb-toast-btn-close-ml)
}

.parent-toast-relative {
    position: relative
}

.toast-absolute {
    position: absolute
}

.toast-fixed {
    position: fixed;
    z-index: var(--mdb-toast-zindex)
}

.toast-primary {
    background-color: var(--mdb-primary-bg-subtle);
    color: var(--mdb-primary-text-emphasis);
    border-color: var(--mdb-primary-border-subtle)
}

.toast-primary i {
    color: var(--mdb-primary-text-emphasis)
}

.toast-secondary {
    background-color: var(--mdb-secondary-bg-subtle);
    color: var(--mdb-secondary-text-emphasis);
    border-color: var(--mdb-secondary-border-subtle)
}

.toast-secondary i {
    color: var(--mdb-secondary-text-emphasis)
}

.toast-success {
    background-color: var(--mdb-success-bg-subtle);
    color: var(--mdb-success-text-emphasis);
    border-color: var(--mdb-success-border-subtle)
}

.toast-success i {
    color: var(--mdb-success-text-emphasis)
}

.toast-danger {
    background-color: var(--mdb-danger-bg-subtle);
    color: var(--mdb-danger-text-emphasis);
    border-color: var(--mdb-danger-border-subtle)
}

.toast-danger i {
    color: var(--mdb-danger-text-emphasis)
}

.toast-warning {
    background-color: var(--mdb-warning-bg-subtle);
    color: var(--mdb-warning-text-emphasis);
    border-color: var(--mdb-warning-border-subtle)
}

.toast-warning i {
    color: var(--mdb-warning-text-emphasis)
}

.toast-info {
    background-color: var(--mdb-info-bg-subtle);
    color: var(--mdb-info-text-emphasis);
    border-color: var(--mdb-info-border-subtle)
}

.toast-info i {
    color: var(--mdb-info-text-emphasis)
}

.toast-light {
    background-color: var(--mdb-light-bg-subtle);
    color: var(--mdb-light-text-emphasis);
    border-color: var(--mdb-light-border-subtle)
}

.toast-light i {
    color: var(--mdb-light-text-emphasis)
}

.toast-dark {
    background-color: var(--mdb-dark-bg-subtle);
    color: var(--mdb-dark-text-emphasis);
    border-color: var(--mdb-dark-border-subtle)
}

.toast-dark i {
    color: var(--mdb-dark-text-emphasis)
}

.tooltip {
    --mdb-tooltip-font-size: 14px
}

.tooltip.show {
    opacity: 1
}

.tooltip .tooltip-arrow {
    display: none
}

.tooltip-inner {
    font-size: var(--mdb-tooltip-font-size)
}

.popover {
    --mdb-popover-border-bottom-width: 2px
}

.popover .popover-arrow {
    display: none
}

.popover-header {
    border-bottom: var(--mdb-popover-border-bottom-width) solid var(--mdb-popover-border-color)
}

.nav-pills.menu-sidebar .nav-link {
    --mdb-scrollspy-menu-sidebar-font-size: 0.8rem;
    --mdb-scrollspy-menu-sidebar-color: var(--mdb-body-color);
    --mdb-scrollspy-menu-sidebar-line-height: 1.1rem;
    --mdb-scrollspy-menu-sidebar-padding-x: 5px;
    --mdb-scrollspy-menu-sidebar-font-weight: 400;
    --mdb-scrollspy-menu-sidebar-transition: all 0.2s ease-in-out;
    --mdb-scrollspy-menu-sidebar-margin-y: 3px;
    font-size: var(--mdb-scrollspy-menu-sidebar-font-size);
    background-color: rgba(0, 0, 0, 0);
    color: var(--mdb-scrollspy-menu-sidebar-color);
    line-height: var(--mdb-scrollspy-menu-sidebar-line-height);
    padding: 0 var(--mdb-scrollspy-menu-sidebar-padding-x);
    font-weight: var(--mdb-scrollspy-menu-sidebar-font-weight);
    transition: var(--mdb-scrollspy-menu-sidebar-transition);
    text-transform: initial;
    margin-top: var(--mdb-scrollspy-menu-sidebar-margin-y);
    margin-bottom: var(--mdb-scrollspy-menu-sidebar-margin-y)
}

.nav-pills.menu-sidebar .nav-link.active,
.nav-pills.menu-sidebar .show>.nav-link {
    --mdb-scrollspy-menu-sidebar-active-color: #3b71ca;
    --mdb-scrollspy-menu-sidebar-active-font-weight: 600;
    --mdb-scrollspy-menu-sidebar-active-border-width: 0.125rem;
    --mdb-scrollspy-menu-sidebar-active-border-color: #3b71ca;
    background-color: rgba(0, 0, 0, 0);
    box-shadow: none;
    color: var(--mdb-scrollspy-menu-sidebar-active-color);
    font-weight: var(--mdb-scrollspy-menu-sidebar-active-font-weight);
    border-left: var(--mdb-scrollspy-menu-sidebar-active-border-width) solid var(--mdb-scrollspy-menu-sidebar-active-border-color);
    border-radius: 0
}

.nav-pills.menu-sidebar .collapsible-scrollspy~.nav {
    --mdb-scrollspy-collapsible-nav-transition-time: 0.5s;
    transition: height var(--mdb-scrollspy-collapsible-nav-transition-time) ease;
    flex-wrap: nowrap
}

.ripple-surface {
    position: relative;
    overflow: hidden;
    display: inline-block;
    vertical-align: bottom
}

.ripple-surface-unbound {
    overflow: visible
}

.ripple-wave {
    --mdb-ripple-wave-cubicBezier: cubic-bezier(0, 0, 0.15, 1);
    --mdb-ripple-wave-border-radius: 50%;
    --mdb-ripple-wave-opacity: 0.5;
    --mdb-ripple-wave-transform: scale(0);
    --mdb-ripple-wave-z-index: 999;
    --mdb-ripple-wave-active-transform: scale(1);
    background-image: radial-gradient(circle, rgba(0, 0, 0, 0.2) 0, rgba(0, 0, 0, 0.3) 40%, rgba(0, 0, 0, 0.4) 50%, rgba(0, 0, 0, 0.5) 60%, rgba(0, 0, 0, 0) 70%);
    border-radius: var(--mdb-ripple-wave-border-radius);
    opacity: var(--mdb-ripple-wave-opacity);
    pointer-events: none;
    position: absolute;
    touch-action: none;
    transform: var(--mdb-ripple-wave-transform);
    transition-property: transform, opacity;
    transition-timing-function: var(--mdb-ripple-wave-cubicBezier), var(--mdb-ripple-wave-cubicBezier);
    z-index: var(--mdb-ripple-wave-z-index)
}

.ripple-wave.active {
    transform: var(--mdb-ripple-wave-active-transform);
    opacity: 0
}

.btn .ripple-wave {
    background-image: radial-gradient(circle, rgba(255, 255, 255, 0.2) 0, rgba(255, 255, 255, 0.3) 40%, rgba(255, 255, 255, 0.4) 50%, rgba(255, 255, 255, 0.5) 60%, rgba(255, 255, 255, 0) 70%)
}

.input-wrapper .ripple-wave {
    background-image: radial-gradient(circle, rgba(255, 255, 255, 0.2) 0, rgba(255, 255, 255, 0.3) 40%, rgba(255, 255, 255, 0.4) 50%, rgba(255, 255, 255, 0.5) 60%, rgba(255, 255, 255, 0) 70%)
}

.ripple-surface-primary .ripple-wave {
    background-image: radial-gradient(circle, rgba(59, 113, 202, 0.2) 0, rgba(59, 113, 202, 0.3) 40%, rgba(59, 113, 202, 0.4) 50%, rgba(59, 113, 202, 0.5) 60%, rgba(59, 113, 202, 0) 70%)
}

.ripple-surface-secondary .ripple-wave {
    background-image: radial-gradient(circle, rgba(227, 235, 247, 0.2) 0, rgba(227, 235, 247, 0.3) 40%, rgba(227, 235, 247, 0.4) 50%, rgba(227, 235, 247, 0.5) 60%, rgba(227, 235, 247, 0) 70%)
}

.ripple-surface-success .ripple-wave {
    background-image: radial-gradient(circle, rgba(20, 164, 77, 0.2) 0, rgba(20, 164, 77, 0.3) 40%, rgba(20, 164, 77, 0.4) 50%, rgba(20, 164, 77, 0.5) 60%, rgba(20, 164, 77, 0) 70%)
}

.ripple-surface-danger .ripple-wave {
    background-image: radial-gradient(circle, rgba(220, 76, 100, 0.2) 0, rgba(220, 76, 100, 0.3) 40%, rgba(220, 76, 100, 0.4) 50%, rgba(220, 76, 100, 0.5) 60%, rgba(220, 76, 100, 0) 70%)
}

.ripple-surface-warning .ripple-wave {
    background-image: radial-gradient(circle, rgba(228, 161, 27, 0.2) 0, rgba(228, 161, 27, 0.3) 40%, rgba(228, 161, 27, 0.4) 50%, rgba(228, 161, 27, 0.5) 60%, rgba(228, 161, 27, 0) 70%)
}

.ripple-surface-info .ripple-wave {
    background-image: radial-gradient(circle, rgba(84, 180, 211, 0.2) 0, rgba(84, 180, 211, 0.3) 40%, rgba(84, 180, 211, 0.4) 50%, rgba(84, 180, 211, 0.5) 60%, rgba(84, 180, 211, 0) 70%)
}

.ripple-surface-light .ripple-wave {
    background-image: radial-gradient(circle, rgba(251, 251, 251, 0.2) 0, rgba(251, 251, 251, 0.3) 40%, rgba(251, 251, 251, 0.4) 50%, rgba(251, 251, 251, 0.5) 60%, rgba(251, 251, 251, 0) 70%)
}

.ripple-surface-dark .ripple-wave {
    background-image: radial-gradient(circle, rgba(51, 45, 45, 0.2) 0, rgba(51, 45, 45, 0.3) 40%, rgba(51, 45, 45, 0.4) 50%, rgba(51, 45, 45, 0.5) 60%, rgba(51, 45, 45, 0) 70%)
}

.range {
    --mdb-range-thumb-height: 30px;
    --mdb-range-thumb-width: 30px;
    --mdb-range-thumb-top: -35px;
    --mdb-range-thumb-margin-left: -15px;
    --mdb-range-thumb-border-radius: 50% 50% 50% 0;
    --mdb-range-thumb-transform: scale(0);
    --mdb-range-thumb-transition: transform 0.2s ease-in-out;
    --mdb-range-thumb-value-font-size: 12px;
    --mdb-range-thumb-value-line-height: 30px;
    --mdb-range-thumb-value-color: #fff;
    --mdb-range-thumb-value-font-weight: 500;
    --mdb-range-thumb-background: #3b71ca;
    position: relative
}

.range .thumb {
    position: absolute;
    display: block;
    height: var(--mdb-range-thumb-height);
    width: var(--mdb-range-thumb-width);
    top: var(--mdb-range-thumb-top);
    margin-left: var(--mdb-range-thumb-margin-left);
    text-align: center;
    border-radius: var(--mdb-range-thumb-border-radius);
    transform: var(--mdb-range-thumb-transform);
    transform-origin: bottom;
    transition: var(--mdb-range-thumb-transition)
}

.range .thumb:after {
    position: absolute;
    display: block;
    content: "";
    transform: translateX(-50%);
    width: 100%;
    height: 100%;
    top: 0;
    border-radius: var(--mdb-range-thumb-border-radius);
    transform: rotate(-45deg);
    background: var(--mdb-range-thumb-background);
    z-index: -1
}

.range .thumb .thumb-value {
    display: block;
    font-size: var(--mdb-range-thumb-value-font-size);
    line-height: var(--mdb-range-thumb-value-line-height);
    color: var(--mdb-range-thumb-value-color);
    font-weight: var(--mdb-range-thumb-value-font-weight);
    z-index: 2
}

.range .thumb.thumb-active {
    transform: scale(1)
}

.accordion-button:not(.collapsed):focus {
    box-shadow: var(--mdb-accordion-btn-focus-box-shadow)
}

.accordion-button:focus {
    border-color: var(--mdb-accordion-btn-focus-border-color);
    outline: 0;
    box-shadow: none
}

.accordion-flush {
    --mdb-accordion-flush-btn-box-shadow: inset 0 -2px 0 var(--mdb-divider-color);
    --mdb-accordion-flush-border-bottom: 2px solid var(--mdb-divider-color)
}

.accordion-flush .accordion-button:not(.collapsed) {
    box-shadow: var(--mdb-accordion-flush-btn-box-shadow)
}

.accordion-flush .accordion-item {
    border-bottom: var(--mdb-accordion-flush-border-bottom)
}

.accordion-borderless {
    --mdb-accordion-borderless-btn-border-radius: 0.5rem;
    --mdb-accordion-borderless-btn-bg: var(--mdb-primary-bg-subtle);
    --mdb-accordion-borderless-btn-color: var(--mdb-primary-text-emphasis)
}

.accordion-borderless .accordion-item {
    border: 0
}

.accordion-borderless .accordion-item .accordion-button {
    border-radius: var(--mdb-accordion-borderless-btn-border-radius)
}

.accordion-borderless .accordion-item .accordion-button:not(.collapsed) {
    background-color: var(--mdb-accordion-borderless-btn-bg);
    color: var(--mdb-accordion-borderless-btn-color);
    box-shadow: none
}

.modal {
    --mdb-modal-top-left-top: 10px;
    --mdb-modal-top-left-left: 10px;
    --mdb-modal-top-right-top: 10px;
    --mdb-modal-top-right-right: 10px;
    --mdb-modal-bottom-left-bottom: 10px;
    --mdb-modal-bottom-left-left: 10px;
    --mdb-modal-bottom-right-bottom: 10px;
    --mdb-modal-bottom-right-right: 10px;
    --mdb-modal-fade-top-transform: translate3d(0, -25%, 0);
    --mdb-modal-fade-right-transform: translate3d(25%, 0, 0);
    --mdb-modal-fade-bottom-transform: translate3d(0, 25%, 0);
    --mdb-modal-fade-left-transform: translate3d(-25%, 0, 0);
    --mdb-modal-side-right: 10px;
    --mdb-modal-side-bottom: 10px;
    --mdb-modal-non-invasive-box-shadow: 0 2px 6px -1px rgba(var(--mdb-box-shadow-color-rgb), 0.07), 0 6px 18px -1px rgba(var(--mdb-box-shadow-color-rgb), 0.04);
    --mdb-modal-non-invasive-box-shadow-top: 0 -10px 20px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.05)
}

@media(min-width: 768px) {
    .modal .modal-dialog.modal-top {
        top: 0
    }

    .modal .modal-dialog.modal-left {
        left: 0
    }

    .modal .modal-dialog.modal-right {
        right: 0
    }

    .modal .modal-dialog.modal-top-left {
        top: var(--mdb-modal-top-left-top);
        left: var(--mdb-modal-top-left-left)
    }

    .modal .modal-dialog.modal-top-right {
        top: var(--mdb-modal-top-right-top);
        right: var(--mdb-modal-top-right-right)
    }

    .modal .modal-dialog.modal-bottom-left {
        bottom: var(--mdb-modal-bottom-left-bottom);
        left: var(--mdb-modal-bottom-left-left)
    }

    .modal .modal-dialog.modal-bottom-right {
        right: var(--mdb-modal-bottom-right-right);
        bottom: var(--mdb-modal-bottom-right-bottom)
    }
}

.modal .modal-dialog.modal-bottom {
    bottom: 0
}

.modal.fade.top:not(.show) .modal-dialog {
    transform: var(--mdb-modal-fade-top-transform)
}

.modal.fade.right:not(.show) .modal-dialog {
    transform: var(--mdb-modal-fade-right-transform)
}

.modal.fade.bottom:not(.show) .modal-dialog {
    transform: var(--mdb-modal-fade-bottom-transform)
}

.modal.fade.left:not(.show) .modal-dialog {
    transform: var(--mdb-modal-fade-left-transform)
}

@media(min-width: 992px) {
    .modal .modal-side {
        position: absolute;
        width: 100%;
        right: var(--mdb-modal-side-right);
        bottom: var(--mdb-modal-side-bottom);
        margin: 0
    }
}

.modal .modal-frame {
    position: absolute;
    max-width: 100%;
    width: 100%;
    margin: 0
}

.modal-open .modal.frame {
    overflow-y: hidden
}

.modal-non-invasive-open {
    overflow-y: auto
}

.modal-non-invasive-open .modal.modal-non-invasive-show {
    display: table
}

@media(min-width: 992px) {
    .modal-non-invasive-open .modal.modal-non-invasive-show .modal-dialog.modal-bottom-right {
        bottom: 0
    }

    .modal-non-invasive-open .modal.modal-non-invasive-show .modal-dialog.modal-bottom-left {
        bottom: 0
    }

    .modal-non-invasive-open .modal.modal-non-invasive-show .modal-side {
        bottom: 0
    }

    .modal-non-invasive-open .modal.modal-non-invasive-show.modal.frame.bottom {
        box-shadow: var(--mdb-modal-non-invasive-box-shadow-top)
    }

    .modal-non-invasive-open .modal.modal-non-invasive-show.modal.frame.bottom .modal-content {
        box-shadow: var(--mdb-modal-non-invasive-box-shadow-top)
    }

    .modal-non-invasive-open .modal.modal-non-invasive-show.modal.frame.top {
        box-shadow: var(--mdb-modal-non-invasive-box-shadow)
    }

    .modal-non-invasive-open .modal.modal-non-invasive-show .modal-side.modal-bottom-right .modal-content {
        box-shadow: var(--mdb-modal-non-invasive-box-shadow-top)
    }

    .modal-non-invasive-open .modal.modal-non-invasive-show .modal-side.modal-bottom-left .modal-content {
        box-shadow: var(--mdb-modal-non-invasive-box-shadow-top)
    }
}

.modal-non-invasive-open .modal.modal-non-invasive-show .modal-dialog.modal-bottom-right {
    right: 0
}

.modal-non-invasive-open .modal.modal-non-invasive-show .modal-dialog.modal-bottom-left {
    left: 0
}

.modal-non-invasive-open .modal.modal-non-invasive-show .modal-dialog.modal-top-left {
    left: 0
}

.modal-non-invasive-open .modal.modal-non-invasive-show .modal-side {
    right: 0
}

.ps {
    --mdb-scrollbar-rail-x-y-transition-opacity-bg: background-color 0.2s linear, opacity 0.2s linear;
    --mdb-scrollbar-z-index: 1035;
    --mdb-scrollbar-rail-x-y-length: 0.9375rem;
    --mdb-scrollbar-rail-x-y-opacity: 0.6;
    --mdb-scrollbar-rail-x-y-hover-opacity: 0.9;
    --mdb-scrollbar-rail-x-y-bg-color: var(--mdb-scrollbar-rail-bg);
    --mdb-scrollbar-rail-x-y-clicking-length: 0.6875rem;
    --mdb-scrollbar-rail-x-transition-height-bg: background-color 0.2s linear, height 0.2s ease-in-out;
    --mdb-scrollbar-rail-y-transition-width-bg: background-color 0.2s linear, width 0.2s ease-in-out;
    --mdb-scrollbar-thumb-x-y-color: var(--mdb-scrollbar-thumb-bg);
    --mdb-scrollbar-thumb-x-y-border-radius: 0.375rem;
    --mdb-scrollbar-thumb-x-y-length: 0.375rem;
    --mdb-scrollbar-thumb-x-y-position-length: 0.125rem;
    overflow: hidden !important;
    overflow-anchor: none;
    touch-action: auto
}

.ps__rail-x,
.ps__rail-y {
    display: none;
    opacity: 0;
    transition: var(--mdb-scrollbar-rail-x-y-transition-opacity-bg);
    position: absolute;
    z-index: var(--mdb-scrollbar-z-index)
}

.ps__rail-x {
    height: var(--mdb-scrollbar-rail-x-y-length);
    bottom: 0
}

.ps__rail-y {
    width: var(--mdb-scrollbar-rail-x-y-length);
    right: 0
}

.ps--active-x>.ps__rail-x,
.ps--active-y>.ps__rail-y {
    display: block;
    background-color: rgba(0, 0, 0, 0)
}

.ps:hover>.ps__rail-x,
.ps:hover>.ps__rail-y {
    opacity: var(--mdb-scrollbar-rail-x-y-opacity)
}

.ps--focus>.ps__rail-x,
.ps--focus>.ps__rail-y {
    opacity: var(--mdb-scrollbar-rail-x-y-opacity)
}

.ps--scrolling-x>.ps__rail-x,
.ps--scrolling-y>.ps__rail-y {
    opacity: var(--mdb-scrollbar-rail-x-y-opacity)
}

.ps .ps__rail-x:hover,
.ps .ps__rail-y:hover,
.ps .ps__rail-x:focus,
.ps .ps__rail-y:focus,
.ps .ps__rail-x.ps--clicking,
.ps .ps__rail-y.ps--clicking {
    background-color: var(--mdb-scrollbar-rail-x-y-bg-color);
    opacity: var(--mdb-scrollbar-rail-x-y-hover-opacity)
}

.ps__thumb-x,
.ps__thumb-y {
    background-color: var(--mdb-scrollbar-thumb-x-y-color);
    border-radius: var(--mdb-scrollbar-thumb-x-y-border-radius);
    position: absolute
}

.ps__thumb-x {
    transition: var(--mdb-scrollbar-rail-x-transition-height-bg);
    height: var(--mdb-scrollbar-thumb-x-y-length);
    bottom: var(--mdb-scrollbar-thumb-x-y-position-length)
}

.ps__thumb-y {
    transition: var(--mdb-scrollbar-rail-y-transition-width-bg);
    width: var(--mdb-scrollbar-thumb-x-y-length);
    right: var(--mdb-scrollbar-thumb-x-y-position-length)
}

.ps__rail-x:hover>.ps__thumb-x,
.ps__rail-x:focus>.ps__thumb-x,
.ps__rail-x.ps--clicking .ps__thumb-x {
    height: var(--mdb-scrollbar-rail-x-y-clicking-length)
}

.ps__rail-y:hover>.ps__thumb-y,
.ps__rail-y:focus>.ps__thumb-y,
.ps__rail-y.ps--clicking .ps__thumb-y {
    width: var(--mdb-scrollbar-rail-x-y-clicking-length)
}

@supports(-ms-overflow-style: none) {
    .ps {
        overflow: auto !important
    }
}

@media screen and (-ms-high-contrast: active),
(-ms-high-contrast: none) {
    .ps {
        overflow: auto !important
    }
}

.sidenav {
    --mdb-sidenav-transform: translateX(-100%)
        /*!rtl:translate(100%)*/
    ;
    --mdb-sidenav-zindex: 1035;
    --mdb-sidenav-color: var(--mdb-surface-color);
    --mdb-sidenav-background-color: var(--mdb-surface-bg);
    --mdb-sidenav-width: 240px;
    --mdb-sidenav-height: 100vh;
    --mdb-sidenav-box-shadow: 0 4px 12px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.07), 0 2px 4px rgba(var(--mdb-box-shadow-color-rgb), 0.05);
    --mdb-sidenav-data-hidden-false-transform: translateX(0%);
    --mdb-sidenav-data-color-light-color: rgba(255, 255, 255, 0.6);
    --mdb-sidenav-data-right-true-transform: translateX(100%);
    --mdb-sidenav-data-slim-collapsed-true-width: 77px;
    --mdb-sidenav-menu-padding: 0.2rem;
    --mdb-sidenav-collapse-sidenav-link-font-size: 0.78rem;
    --mdb-sidenav-collapse-sidenav-link-height: 1.5rem;
    --mdb-sidenav-link-font-size: 0.89rem;
    --mdb-sidenav-link-padding-y: 1rem;
    --mdb-sidenav-link-padding-x: 1.5rem;
    --mdb-sidenav-collapse-sidenav-link-padding-left: 3.4rem;
    --mdb-sidenav-link-height: 3rem;
    --mdb-sidenav-link-border-radius: 5px;
    --mdb-sidenav-link-transition: all 0.3s linear;
    --mdb-sidenav-link-hover-background-color: var(--mdb-highlight-bg-color);
    --mdb-sidenav-link-active-focus-background-color: var(--mdb-highlight-bg-color);
    --mdb-sidenav-link-active-color: #3b71ca;
    --mdb-sidenav-subheading-font-size: 0.6rem;
    --mdb-sidenav-subheading-padding-y: 1rem;
    --mdb-sidenav-subheading-padding-x: 1.5rem;
    --mdb-sidenav-subheading-fw: 700;
    --mdb-sidenav-sm-link-pt: 0.4rem;
    --mdb-sidenav-sm-link-pb: 0.4rem;
    --mdb-sidenav-rotate-icon-margin-right: 0.8rem;
    --mdb-sidenav-rotate-icon-transition: transform 0.3s;
    --mdb-sidenav-light-color: rgba(255, 255, 255, 0.6);
    top: 0;
    left: 0;
    transform: var(--mdb-sidenav-transform);
    position: fixed;
    z-index: var(--mdb-sidenav-zindex);
    color: var(--mdb-sidenav-color);
    background-color: var(--mdb-sidenav-background-color);
    overflow: hidden;
    width: var(--mdb-sidenav-width);
    height: var(--mdb-sidenav-height);
    box-shadow: var(--mdb-sidenav-box-shadow)
}

.sidenav[data-mdb-hidden=false] {
    transform: var(--mdb-sidenav-data-hidden-false-transform)
}

.sidenav[data-mdb-color=light] {
    color: var(--mdb-sidenav-data-color-light-color)
}

.sidenav[data-mdb-right=true] {
    right: 0;
    left: unset;
    transform: var(--mdb-sidenav-data-right-true-transform)
}

.sidenav[data-mdb-position=absolute] {
    position: absolute;
    height: 100%
}

.sidenav[data-mdb-position=relative] {
    position: relative;
    height: 100%
}

.sidenav [data-mdb-slim=true] {
    display: none
}

.sidenav[data-mdb-slim-collapsed=true] {
    width: var(--mdb-sidenav-data-slim-collapsed-true-width)
}

.sidenav[data-mdb-slim-collapsed=true] [data-mdb-slim=false] {
    display: none
}

.sidenav[data-mdb-slim-collapsed=true] [data-mdb-slim=true] {
    display: unset
}

.sidenav-menu,
.sidenav-collapse {
    list-style: none;
    position: relative;
    padding: 0 var(--mdb-sidenav-menu-padding);
    margin: 0
}

.sidenav-collapse {
    display: none;
    padding: 0
}

.sidenav-collapse.show,
.sidenav-collapse.collapsing {
    display: block
}

.sidenav-collapse .sidenav-link {
    font-size: var(--mdb-sidenav-collapse-sidenav-link-font-size);
    height: var(--mdb-sidenav-collapse-sidenav-link-height);
    padding-left: var(--mdb-sidenav-collapse-sidenav-link-padding-left)
}

.sidenav-item {
    position: relative
}

.sidenav-link {
    display: flex;
    align-items: center;
    cursor: pointer;
    font-size: var(--mdb-sidenav-link-font-size);
    padding: var(--mdb-sidenav-link-padding-y) var(--mdb-sidenav-link-padding-x);
    height: var(--mdb-sidenav-link-height);
    color: unset;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    border-radius: var(--mdb-sidenav-link-border-radius);
    transition: var(--mdb-sidenav-link-transition)
}

.sidenav-link:hover {
    color: inherit;
    background-color: var(--mdb-sidenav-link-hover-background-color);
    outline: none
}

.sidenav-link:active,
.sidenav-link:focus {
    color: inherit;
    background-color: var(--mdb-sidenav-link-active-focus-background-color);
    outline: none
}

.sidenav-link.active {
    color: var(--mdb-sidenav-link-active-color)
}

.sidenav-link i {
    color: #9fa6b2
}

.sidenav-subheading {
    color: unset;
    text-transform: uppercase;
    font-size: var(--mdb-sidenav-subheading-font-size);
    padding: var(--mdb-sidenav-subheading-padding-y) var(--mdb-sidenav-subheading-padding-x);
    font-weight: var(--mdb-sidenav-subheading-fw)
}

.sidenav-sm .sidenav-link {
    padding-top: var(--mdb-sidenav-sm-link-pt);
    padding-bottom: var(--mdb-sidenav-sm-link-pb);
    height: initial
}

.rotate-icon {
    position: absolute;
    right: 0;
    margin-left: auto;
    margin-right: var(--mdb-sidenav-rotate-icon-margin-right);
    transition: var(--mdb-sidenav-rotate-icon-transition)
}

.sidenav-backdrop {
    --mdb-sidenav-backdrop-zindex: 1034;
    --mdb-sidenav-backdrop-background-color: rgba(0, 0, 0, var(--mdb-sidenav-backdrop-opacity));
    z-index: var(--mdb-sidenav-backdrop-zindex);
    top: 0;
    left: 0;
    background-color: var(--mdb-sidenav-backdrop-background-color)
}

.sidenav-light {
    color: var(--mdb-sidenav-light-color)
}

.sidenav-slim {
    --mdb-sidenav-slim-link-padding-left: 1rem
}

.sidenav-slim .sidenav-link {
    padding-left: var(--mdb-sidenav-slim-link-padding-left)
}

.sidenav-primary .sidenav-item .sidenav-link:hover {
    color: inherit;
    background-color: rgba(59, 113, 202, .05)
}

.sidenav-primary .sidenav-link:active,
.sidenav-primary .sidenav-link:focus {
    color: inherit;
    background-color: rgba(59, 113, 202, .05)
}

.sidenav-primary .sidenav-link.active {
    color: inherit
}

.sidenav-secondary .sidenav-item .sidenav-link:hover {
    color: inherit;
    background-color: rgba(159, 166, 178, .05)
}

.sidenav-secondary .sidenav-link:active,
.sidenav-secondary .sidenav-link:focus {
    color: inherit;
    background-color: rgba(159, 166, 178, .05)
}

.sidenav-secondary .sidenav-link.active {
    color: inherit
}

.sidenav-success .sidenav-item .sidenav-link:hover {
    color: inherit;
    background-color: rgba(20, 164, 77, .05)
}

.sidenav-success .sidenav-link:active,
.sidenav-success .sidenav-link:focus {
    color: inherit;
    background-color: rgba(20, 164, 77, .05)
}

.sidenav-success .sidenav-link.active {
    color: inherit
}

.sidenav-danger .sidenav-item .sidenav-link:hover {
    color: inherit;
    background-color: rgba(220, 76, 100, .05)
}

.sidenav-danger .sidenav-link:active,
.sidenav-danger .sidenav-link:focus {
    color: inherit;
    background-color: rgba(220, 76, 100, .05)
}

.sidenav-danger .sidenav-link.active {
    color: inherit
}

.sidenav-warning .sidenav-item .sidenav-link:hover {
    color: inherit;
    background-color: rgba(228, 161, 27, .05)
}

.sidenav-warning .sidenav-link:active,
.sidenav-warning .sidenav-link:focus {
    color: inherit;
    background-color: rgba(228, 161, 27, .05)
}

.sidenav-warning .sidenav-link.active {
    color: inherit
}

.sidenav-info .sidenav-item .sidenav-link:hover {
    color: inherit;
    background-color: rgba(84, 180, 211, .05)
}

.sidenav-info .sidenav-link:active,
.sidenav-info .sidenav-link:focus {
    color: inherit;
    background-color: rgba(84, 180, 211, .05)
}

.sidenav-info .sidenav-link.active {
    color: inherit
}

.sidenav-light .sidenav-item .sidenav-link:hover {
    color: inherit;
    background-color: rgba(251, 251, 251, .05)
}

.sidenav-light .sidenav-link:active,
.sidenav-light .sidenav-link:focus {
    color: inherit;
    background-color: rgba(251, 251, 251, .05)
}

.sidenav-light .sidenav-link.active {
    color: inherit
}

.sidenav-dark .sidenav-item .sidenav-link:hover {
    color: inherit;
    background-color: rgba(51, 45, 45, .05)
}

.sidenav-dark .sidenav-link:active,
.sidenav-dark .sidenav-link:focus {
    color: inherit;
    background-color: rgba(51, 45, 45, .05)
}

.sidenav-dark .sidenav-link.active {
    color: inherit
}

.animation {
    --mdb-animation-delay-1s: 1s;
    --mdb-animation-delay-2s: 3s;
    --mdb-animation-delay-3s: 3s;
    --mdb-animation-delay-4s: 4s;
    --mdb-animation-delay-5s: 5s;
    --mdb-animation-fast-duration: 800ms;
    --mdb-animation-faster-duration: 500ms;
    --mdb-animation-slow-duration: 2s;
    --mdb-animation-slower-duration: 3s
}

.animation.infinite {
    animation-iteration-count: infinite
}

.animation.delay-1s {
    animation-delay: var(--mdb-animation-delay-1s)
}

.animation.delay-2s {
    animation-delay: var(--mdb-animation-delay-2s)
}

.animation.delay-3s {
    animation-delay: var(--mdb-animation-delay-3s)
}

.animation.delay-4s {
    animation-delay: var(--mdb-animation-delay-4s)
}

.animation.delay-5s {
    animation-delay: var(--mdb-animation-delay-5s)
}

.animation.fast {
    animation-duration: var(--mdb-animation-fast-duration)
}

.animation.faster {
    animation-duration: var(--mdb-animation-faster-duration)
}

.animation.slow {
    animation-duration: var(--mdb-animation-slow-duration)
}

.animation.slower {
    animation-duration: var(--mdb-animation-slower-duration)
}

@keyframes fade-in-down {
    from {
        opacity: 0;
        transform: var(--mdb-animation-fade-in-down-transform-from)
    }

    to {
        opacity: 1;
        transform: var(--mdb-animation-fade-in-down-transform-to)
    }
}

.fade-in-down {
    --mdb-animation-fade-in-down-transform-from: translate3d(0, -100%, 0);
    --mdb-animation-fade-in-down-transform-to: translate3d(0, 0, 0);
    animation-name: fade-in-down
}

@keyframes fade-in-left {
    from {
        opacity: 0;
        transform: var(--mdb-animation-fade-in-left-transform-from)
    }

    to {
        opacity: 1;
        transform: var(--mdb-animation-fade-in-left-transform-to)
    }
}

.fade-in-left {
    --mdb-animation-fade-in-left-transform-from: translate3d(-100%, 0, 0);
    --mdb-animation-fade-in-left-transform-to: translate3d(0, 0, 0);
    animation-name: fade-in-left
}

@keyframes fade-in-right {
    from {
        opacity: 0;
        transform: var(--mdb-animation-fade-in-right-transform-from)
    }

    to {
        opacity: 1;
        transform: var(--mdb-animation-fade-in-right-transform-to)
    }
}

.fade-in-right {
    --mdb-animation-fade-in-right-transform-from: translate3d(100%, 0, 0);
    --mdb-animation-fade-in-right-transform-to: translate3d(0, 0, 0);
    animation-name: fade-in-right
}

@keyframes fade-in-up {
    from {
        opacity: 0;
        transform: var(--mdb-animation-fade-in-up-transform-from)
    }

    to {
        opacity: 1;
        transform: var(--mdb-animation-fade-in-up-transform-to)
    }
}

.fade-in-up {
    --mdb-animation-fade-in-up-transform-from: translate3d(0, 100%, 0);
    --mdb-animation-fade-in-up-transform-to: translate3d(0, 0, 0);
    animation-name: fade-in-up
}

@keyframes fade-out-down {
    from {
        opacity: 1
    }

    to {
        opacity: 0;
        transform: var(--mdb-animation-fade-out-down-transform-to)
    }
}

.fade-out-down {
    --mdb-animation-fade-out-down-transform-to: translate3d(0, 100%, 0);
    animation-name: fade-out-down
}

@keyframes fade-out-left {
    from {
        opacity: 1
    }

    to {
        opacity: 0;
        transform: var(--mdb-animation-fade-out-left-transform-to)
    }
}

.fade-out-left {
    --mdb-animation-fade-out-left-transform-to: translate3d(-100%, 0, 0);
    animation-name: fade-out-left
}

@keyframes fade-out-right {
    from {
        opacity: 1
    }

    to {
        opacity: 0;
        transform: var(--mdb-animation-fade-out-right-transform-to)
    }
}

.fade-out-right {
    --mdb-animation-fade-out-right-transform-to: translate3d(100%, 0, 0);
    animation-name: fade-out-right
}

@keyframes fade-out-up {
    from {
        opacity: 1
    }

    to {
        opacity: 0;
        transform: var(--mdb-animation-fade-out-up-transform-to)
    }
}

.fade-out-up {
    --mdb-animation-fade-out-up-transform-to: translate3d(0, -100%, 0);
    animation-name: fade-out-up
}

@keyframes slide-in-down {
    from {
        visibility: visible;
        transform: var(--mdb-animation-slide-in-down-transform-from)
    }

    to {
        transform: var(--mdb-animation-slide-in-down-transform-to)
    }
}

.slide-in-down {
    --mdb-animation-slide-in-down-transform-from: translate3d(0, -100%, 0);
    --mdb-animation-slide-in-down-transform-to: translate3d(0, 0, 0);
    animation-name: slide-in-down
}

@keyframes slide-in-left {
    from {
        visibility: visible;
        transform: var(--mdb-animation-slide-in-left-transform-from)
    }

    to {
        transform: var(--mdb-animation-slide-in-left-transform-to)
    }
}

.slide-in-left {
    --mdb-animation-slide-in-left-transform-from: translate3d(-100%, 0, 0);
    --mdb-animation-slide-in-left-transform-to: translate3d(0, 0, 0);
    animation-name: slide-in-left
}

@keyframes slide-in-right {
    from {
        visibility: visible;
        transform: var(--mdb-animation-slide-in-right-transform-from)
    }

    to {
        transform: var(--mdb-animation-slide-in-right-transform-to)
    }
}

.slide-in-right {
    --mdb-animation-slide-in-right-transform-from: translate3d(100%, 0, 0);
    --mdb-animation-slide-in-right-transform-to: translate3d(0, 0, 0);
    animation-name: slide-in-right
}

@keyframes slide-in-up {
    from {
        visibility: visible;
        transform: var(--mdb-animation-slide-in-up-transform-from)
    }

    to {
        transform: var(--mdb-animation-slide-in-up-transform-to)
    }
}

.slide-in-up {
    --mdb-animation-slide-in-up-transform-from: translate3d(0, 100%, 0);
    --mdb-animation-slide-in-up-transform-to: translate3d(0, 0, 0);
    animation-name: slide-in-up
}

@keyframes slide-out-down {
    from {
        transform: var(--mdb-animation-slide-out-down-transform-from)
    }

    to {
        visibility: hidden;
        transform: var(--mdb-animation-slide-out-down-transform-to)
    }
}

.slide-out-down {
    --mdb-animation-slide-out-down-transform-from: translate3d(0, 0, 0);
    --mdb-animation-slide-out-down-transform-to: translate3d(0, 100%, 0);
    animation-name: slide-out-down
}

@keyframes slide-out-left {
    from {
        transform: var(--mdb-animation-slide-out-left-transform-from)
    }

    to {
        visibility: hidden;
        transform: var(--mdb-animation-slide-out-left-transform-to)
    }
}

.slide-out-left {
    --mdb-animation-slide-out-left-transform-from: translate3d(0, 0, 0);
    --mdb-animation-slide-out-left-transform-to: translate3d(-100%, 0, 0);
    animation-name: slide-out-left
}

@keyframes slide-out-right {
    from {
        transform: var(--mdb-animation-slide-out-right-transform-from)
    }

    to {
        visibility: hidden;
        transform: var(--mdb-animation-slide-out-right-transform-to)
    }
}

.slide-out-right {
    --mdb-animation-slide-out-right-transform-from: translate3d(0, 0, 0);
    --mdb-animation-slide-out-right-transform-to: translate3d(100%, 0, 0);
    animation-name: slide-out-right
}

@keyframes slide-out-up {
    from {
        transform: var(--mdb-animation-slide-out-up-transform-from)
    }

    to {
        visibility: hidden;
        transform: var(--mdb-animation-slide-out-up-transform-to)
    }
}

.slide-out-up {
    --mdb-animation-slide-out-up-transform-from: translate3d(0, 0, 0);
    --mdb-animation-slide-out-up-transform-to: translate3d(0, -100%, 0);
    animation-name: slide-out-up
}

@keyframes slide-down {
    from {
        transform: var(--mdb-animation-slide-down-transform-from)
    }

    to {
        transform: var(--mdb-animation-slide-down-transform-to)
    }
}

.slide-down {
    --mdb-animation-slide-down-transform-from: translate3d(0, 0, 0);
    --mdb-animation-slide-down-transform-to: translate3d(0, 100%, 0);
    animation-name: slide-down
}

@keyframes slide-left {
    from {
        transform: var(--mdb-animation-slide-left-transform-from)
    }

    to {
        transform: var(--mdb-animation-slide-left-transform-to)
    }
}

.slide-left {
    --mdb-animation-slide-left-transform-from: translate3d(0, 0, 0);
    --mdb-animation-slide-left-transform-to: translate3d(-100%, 0, 0);
    animation-name: slide-left
}

@keyframes slide-right {
    from {
        transform: var(--mdb-animation-slide-right-transform-from)
    }

    to {
        transform: var(--mdb-animation-slide-right-transform-to)
    }
}

.slide-right {
    --mdb-animation-slide-right-transform-from: translate3d(0, 0, 0);
    --mdb-animation-slide-right-transform-to: translate3d(100%, 0, 0);
    animation-name: slide-right
}

@keyframes slide-up {
    from {
        transform: var(--mdb-animation-slide-up-transform-from)
    }

    to {
        transform: var(--mdb-animation-slide-up-transform-to)
    }
}

.slide-up {
    --mdb-animation-slide-up-transform-from: translate3d(0, 0, 0);
    --mdb-animation-slide-up-transform-to: translate3d(0, -100%, 0);
    animation-name: slide-up
}

@keyframes zoom-in {
    from {
        opacity: 0;
        transform: var(--mdb-animation-zoom-in-transform-from)
    }

    50% {
        opacity: 1
    }
}

.zoom-in {
    --mdb-animation-zoom-in-transform-from: scale3d(0.3, 0.3, 0.3);
    animation-name: zoom-in
}

@keyframes zoom-out {
    from {
        opacity: 1
    }

    50% {
        opacity: 0;
        transform: var(--mdb-animation-zoom-out-transform-50)
    }

    to {
        opacity: 0
    }
}

.zoom-out {
    --mdb-animation-zoom-out-transform-50: scale3d(0.3, 0.3, 0.3);
    animation-name: zoom-out
}

@keyframes tada {
    from {
        transform: var(--mdb-animation-tada-transform-from)
    }

    10%,
    20% {
        transform: var(--mdb-animation-tada-transform-20)
    }

    30%,
    50%,
    70%,
    90% {
        transform: var(--mdb-animation-tada-transform-90)
    }

    40%,
    60%,
    80% {
        transform: var(--mdb-animation-tada-transform-80)
    }

    to {
        transform: var(--mdb-animation-tada-transform-to)
    }
}

.tada {
    --mdb-animation-tada-transform-from: scale3d(1, 1, 1);
    --mdb-animation-tada-transform-20: scale3d(0.9, 0.9, 0.9) rotate3d(0, 0, 1, -3deg);
    --mdb-animation-tada-transform-90: scale3d(1.1, 1.1, 1.1) rotate3d(0, 0, 1, 3deg);
    --mdb-animation-tada-transform-80: scale3d(1.1, 1.1, 1.1) rotate3d(0, 0, 1, -3deg);
    --mdb-animation-tada-transform-to: scale3d(1, 1, 1);
    animation-name: tada
}

@keyframes pulse {
    from {
        transform: var(--mdb-animation-pulse-transform-from)
    }

    50% {
        transform: var(--mdb-animation-pulse-transform-50)
    }

    to {
        transform: var(--mdb-animation-pulse-transform-to)
    }
}

.pulse {
    --mdb-animation-pulse-transform-from: scale3d(1, 1, 1);
    --mdb-animation-pulse-transform-50: scale3d(1.05, 1.05, 1.05);
    --mdb-animation-pulse-transform-to: scale3d(1, 1, 1);
    animation-name: pulse
}

.steps,
.timeline,
.stepper {
    --mdb-steps-transition: height 0.2s ease-in-out;
    position: relative;
    padding: 0;
    margin: 0;
    width: 100%;
    list-style: none;
    overflow: hidden;
    transition: var(--mdb-steps-transition)
}

.steps-step,
.timeline-step,
.stepper-vertical .stepper-step {
    --mdb-steps-step-after-left: 2.45rem;
    --mdb-steps-step-after-width: 1px;
    --mdb-steps-step-after-margin-top: 0.5rem;
    --mdb-steps-step-after-bg: rgba(var(--mdb-emphasis-color-rgb), 0.1);
    height: fit-content;
    position: relative
}

.steps-step-after,
.timeline-step:after,
.stepper-vertical .stepper-step:not(:last-child):after {
    position: absolute;
    left: var(--mdb-steps-step-after-left);
    width: var(--mdb-steps-step-after-width);
    margin-top: var(--mdb-steps-step-after-margin-top);
    content: "";
    background-color: var(--mdb-steps-step-after-bg)
}

.steps-content,
.timeline-content,
.stepper-vertical .stepper-content {
    --mdb-steps-content-padding-y: 1.5rem;
    overflow: hidden;
    padding-top: 0;
    padding-bottom: var(--mdb-steps-content-padding-y);
    padding-right: var(--mdb-steps-content-padding-y)
}

.steps-head-vertical,
.timeline-head,
.stepper-vertical .stepper-head {
    --mdb-steps-head-vertical-padding-top: 1.5rem;
    --mdb-steps-head-vertical-padding-x: 1.5rem;
    padding-left: var(--mdb-steps-head-vertical-padding-x);
    padding-right: var(--mdb-steps-head-vertical-padding-x);
    padding-top: var(--mdb-steps-head-vertical-padding-top)
}

.steps-head-icon-vertical,
.timeline-head-icon,
.stepper-vertical .stepper-head-icon {
    --mdb-steps-head-icon-vertical-margin-right: 0.75rem;
    margin-right: var(--mdb-steps-head-icon-vertical-margin-right)
}

.steps-head-text-after-vertical,
.stepper-vertical .stepper-head-text:after {
    position: absolute
}

.steps-head,
.timeline-head,
.stepper-head {
    --mdb-steps-head-line-height: 1.3;
    --mdb-steps-head-hover-bgc: rgba(var(--mdb-emphasis-color-rgb), 0.025);
    display: flex;
    align-items: center;
    text-decoration: none;
    color: unset;
    line-height: var(--mdb-steps-head-line-height)
}

.steps-head-hover,
.stepper-head:hover {
    background-color: var(--mdb-steps-head-hover-bgc)
}

.steps-head-focus,
.stepper-head:focus {
    outline: none
}

.steps-head-text,
.timeline-head-text,
.stepper-head-text {
    --mdb-steps-head-text-color: rgba(var(--mdb-emphasis-color-rgb), 0.55);
    --mdb-steps-head-text-after-font-size: 0.8rem;
    color: var(--mdb-steps-head-text-color)
}

.steps-head-text-after,
.timeline-head-text:after,
.stepper-head-text:after {
    display: flex;
    font-size: var(--mdb-steps-head-text-after-font-size);
    content: attr(data-content)
}

.steps-head-icon,
.timeline-head-icon,
.stepper-head-icon {
    --mdb-steps-head-icon-font-size: 0.875rem;
    --mdb-steps-head-icon-width: 1.938rem;
    --mdb-steps-head-icon-height: 1.938rem;
    --mdb-steps-head-icon-font-weight: 500;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 100%;
    font-size: var(--mdb-steps-head-icon-font-size);
    width: var(--mdb-steps-head-icon-width);
    height: var(--mdb-steps-head-icon-height);
    font-weight: var(--mdb-steps-head-icon-font-weight)
}

.steps-active-head-text,
.timeline-head-text,
.stepper-active .stepper-head-text {
    --mdb-steps-active-head-text-font-weight: 500;
    font-weight: var(--mdb-steps-active-head-text-font-weight)
}

.stepper {
    --mdb-stepper-padding-x: 1rem;
    --mdb-stepper-step-height: 4.5rem;
    --mdb-stepper-step-head-padding-left: 1.5rem;
    --mdb-stepper-step-head-padding-right: 1.5rem;
    --mdb-stepper-step-head-height: 1px;
    --mdb-stepper-step-head-bg: rgba(var(--mdb-emphasis-color-rgb), 0.1);
    --mdb-stepper-step-head-margin-right: 0.5rem;
    --mdb-stepper-step-head-margin-left: 0.5rem;
    --mdb-stepper-head-icon-margin-y: 1.5rem;
    --mdb-stepper-head-icon-margin-right: 0.5rem;
    --mdb-stepper-vertical-step-top: 3.25rem;
    --mdb-stepper-vertical-step-height: calc(100% - 2.45rem);
    --mdb-stepper-vertical-content-padding-left: 3.75rem;
    --mdb-stepper-vertical-content-transition: height 0.3s ease-in-out, margin-top 0.3s ease-in-out, margin-bottom 0.3s ease-in-out, padding-top 0.3s ease-in-out, padding-bottom 0.3s ease-in-out;
    --mdb-stepper-vertical-head-padding-bottom: 1.5rem;
    --mdb-stepper-mobile-step-margin-y: 1rem;
    --mdb-stepper-mobile-step-head-padding-x: 0.25rem;
    --mdb-stepper-mobile-head-icon-height: 0.5rem;
    --mdb-stepper-mobile-head-icon-width: 0.5rem;
    --mdb-stepper-mobile-content-top: 2.56rem;
    --mdb-stepper-mobile-active-head-icon-bg: var(--mdb-primary);
    --mdb-stepper-mobile-completed-head-icon-bg: var(--mdb-success);
    --mdb-stepper-head-icon-bg: var(--mdb-surface-inverted-bg);
    --mdb-stepper-head-icon-color: var(--mdb-surface-inverted-color);
    --mdb-stepper-completed-head-icon-bg: var(--mdb-success-bg-subtle);
    --mdb-stepper-completed-head-icon-color: var(--mdb-success-text-emphasis);
    --mdb-stepper-active-head-icon-bg: var(--mdb-primary-bg-subtle);
    --mdb-stepper-active-head-icon-color: var(--mdb-primary-text-emphasis);
    --mdb-stepper-invalid-head-icon-bg: var(--mdb-danger-bg-subtle);
    --mdb-stepper-invalid-head-icon-color: var(--mdb-danger-text-emphasis);
    --mdb-stepper-disabled-head-color: rgba(var(--mdb-emphasis-color-rgb), 0.3);
    --mdb-stepper-disabled-head-icon-bg: var(--mdb-surface-inverted-bg);
    --mdb-stepper-disabled-head-icon-color: rgba(var(--mdb-surface-inverted-color-rgb), 0.55);
    --mdb-stepper-mobile-head-padding-y: 0.5rem;
    --mdb-stepper-mobile-head-padding-x: 1rem;
    --mdb-stepper-mobile-footer-height: 2.5rem;
    --mdb-stepper-back-btn-i-margin-right: 0.5rem;
    --mdb-stepper-next-btn-i-margin-left: 0.5rem;
    --mdb-stepper-mobile-progress-bar-height: 0.3rem;
    --mdb-stepper-mobile-progress-height: 0.3rem;
    --mdb-stepper-mobile-progress-background-color: var(--mdb-secondary-bg);
    --mdb-stepper-mobile-active-progress-bar-color: var(--mdb-primary);
    --mdb-stepper-mobile-footer-bg: var(--mdb-stepper-mobile-bg);
    --mdb-stepper-mobile-head-bg: var(--mdb-stepper-mobile-bg);
    --mdb-stepper-mobile-invalid-icon-bg: var(--mdb-danger)
}

.stepper:not(.stepper-vertical) {
    display: flex;
    justify-content: space-between
}

.stepper:not(.stepper-vertical) .stepper-content {
    position: absolute;
    width: 100%;
    padding-right: var(--mdb-stepper-padding-x);
    padding-left: var(--mdb-stepper-padding-x)
}

.stepper:not(.stepper-vertical) .stepper-step {
    flex: auto;
    height: var(--mdb-stepper-step-height)
}

.stepper:not(.stepper-vertical) .stepper-step:first-child .stepper-head {
    padding-left: var(--mdb-stepper-step-head-padding-left)
}

.stepper:not(.stepper-vertical) .stepper-step:last-child .stepper-head {
    padding-right: var(--mdb-stepper-step-head-padding-right)
}

.stepper:not(.stepper-vertical) .stepper-step:not(:first-child) .stepper-head:before {
    flex: 1;
    height: var(--mdb-stepper-step-head-height);
    width: 100%;
    margin-right: var(--mdb-stepper-step-head-margin-right);
    content: "";
    background-color: var(--mdb-stepper-step-head-bg)
}

.stepper:not(.stepper-vertical) .stepper-step:not(:last-child) .stepper-head:after {
    flex: 1;
    height: var(--mdb-stepper-step-head-height);
    width: 100%;
    margin-left: var(--mdb-stepper-step-head-margin-left);
    content: "";
    background-color: var(--mdb-stepper-step-head-bg)
}

.stepper:not(.stepper-vertical) .stepper-head-icon {
    margin-top: var(--mdb-stepper-head-icon-margin-y);
    margin-right: var(--mdb-stepper-head-icon-margin-right);
    margin-bottom: var(--mdb-stepper-head-icon-margin-y);
    margin-left: 0
}

.stepper-vertical .stepper-step:not(:last-child):after {
    top: var(--mdb-stepper-vertical-step-top);
    height: var(--mdb-stepper-vertical-step-height)
}

.stepper-vertical .stepper-content {
    padding-left: var(--mdb-stepper-vertical-content-padding-left);
    transition: var(--mdb-stepper-vertical-content-transition)
}

.stepper-vertical .stepper-content-hide {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    height: 0 !important
}

.stepper-vertical .stepper-head {
    padding-bottom: var(--mdb-stepper-vertical-head-padding-bottom)
}

.stepper.stepper-mobile {
    justify-content: center;
    align-items: flex-end
}

.stepper.stepper-mobile.stepper-progress-bar .stepper-head-icon {
    display: none
}

.stepper.stepper-mobile .stepper-step {
    flex: unset;
    height: fit-content;
    margin-top: var(--mdb-stepper-mobile-step-margin-y);
    margin-bottom: var(--mdb-stepper-mobile-step-margin-y)
}

.stepper.stepper-mobile .stepper-step:not(:last-child) .stepper-head:after {
    margin-left: 0
}

.stepper.stepper-mobile .stepper-step:not(:first-child) .stepper-head:before {
    margin-right: 0
}

.stepper.stepper-mobile .stepper-step:not(:last-child):not(:first-child) .stepper-head {
    padding-left: var(--mdb-stepper-mobile-step-head-padding-x);
    padding-right: var(--mdb-stepper-mobile-step-head-padding-x)
}

.stepper.stepper-mobile .stepper-head-icon {
    font-size: 0;
    margin: 0;
    height: var(--mdb-stepper-mobile-head-icon-height);
    width: var(--mdb-stepper-mobile-head-icon-width);
    z-index: 1
}

.stepper.stepper-mobile .stepper-head-text {
    display: none
}

.stepper.stepper-mobile .stepper-content {
    top: var(--mdb-stepper-mobile-content-top)
}

.stepper.stepper-mobile .stepper-active .stepper-head-icon {
    background-color: var(--mdb-stepper-mobile-active-head-icon-bg)
}

.stepper.stepper-mobile .stepper-completed .stepper-head-icon {
    background-color: var(--mdb-stepper-mobile-completed-head-icon-bg)
}

.stepper.stepper-mobile .stepper-invalid .stepper-head-icon {
    background-color: var(--mdb-stepper-mobile-invalid-icon-bg)
}

.stepper-form {
    display: inherit;
    justify-content: inherit;
    width: inherit;
    position: inherit
}

.stepper-content {
    left: 0
}

.stepper-head {
    cursor: pointer
}

.stepper-head-icon {
    background-color: var(--mdb-stepper-head-icon-bg);
    color: var(--mdb-stepper-head-icon-color)
}

.stepper-completed .stepper-head-icon {
    background-color: var(--mdb-stepper-completed-head-icon-bg);
    color: var(--mdb-stepper-completed-head-icon-color)
}

.stepper-active .stepper-content {
    display: block
}

.stepper-active .stepper-head-icon {
    background-color: var(--mdb-stepper-active-head-icon-bg);
    color: var(--mdb-stepper-active-head-icon-color)
}

.stepper-invalid .stepper-head-icon {
    background-color: var(--mdb-stepper-invalid-head-icon-bg);
    color: var(--mdb-stepper-invalid-head-icon-color)
}

.stepper-disabled .stepper-head {
    cursor: default
}

.stepper-disabled .stepper-head-icon {
    background-color: var(--mdb-stepper-disabled-head-icon-bg);
    color: var(--mdb-stepper-disabled-head-icon-color)
}

.stepper-disabled .stepper-head-text {
    color: var(--mdb-stepper-disabled-head-color)
}

.stepper-mobile-head {
    position: absolute;
    align-self: normal;
    height: fit-content;
    background-color: var(--mdb-stepper-mobile-head-bg);
    width: 100%;
    padding-top: var(--mdb-stepper-mobile-head-padding-y);
    padding-right: var(--mdb-stepper-mobile-head-padding-x);
    padding-bottom: var(--mdb-stepper-mobile-head-padding-y);
    padding-left: var(--mdb-stepper-mobile-head-padding-x)
}

.stepper-mobile-footer {
    position: absolute;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: var(--mdb-stepper-mobile-footer-bg);
    width: 100%;
    height: var(--mdb-stepper-mobile-footer-height)
}

.stepper-back-btn {
    display: block;
    left: 0
}

.stepper-back-btn .btn-link {
    color: unset
}

.stepper-back-btn i {
    margin-right: var(--mdb-stepper-back-btn-i-margin-right)
}

.stepper-next-btn {
    display: block;
    right: 0
}

.stepper-next-btn .btn-link {
    color: unset
}

.stepper-next-btn i {
    margin-left: var(--mdb-stepper-next-btn-i-margin-left)
}

.stepper-mobile-progress-bar {
    height: var(--mdb-stepper-mobile-progress-bar-height);
    background-color: var(--mdb-stepper-mobile-active-progress-bar-color);
    width: 0
}

.stepper-mobile-progress {
    height: var(--mdb-stepper-mobile-progress-height);
    flex-grow: 100;
    background-color: var(--mdb-stepper-mobile-progress-background-color)
}

.timeline {
    --mdb-timeline-step-top: 2.94rem;
    --mdb-timeline-step-height: calc(100% - 1.94rem);
    --mdb-timeline-content-padding-left: 4.25rem;
    --mdb-timeline-head-padding-bottom: 0.5rem;
    --mdb-timeline-step-sm-left: 1.8rem;
    --mdb-timeline-step-sm-top: 2rem;
    --mdb-timeline-head-sm-margin-right: 1rem;
    --mdb-timeline-head-sm-bg: #dfdfdf;
    --mdb-timeline-head-sm-height: 0.7rem;
    --mdb-timeline-head-sm-width: 0.7rem;
    --mdb-timeline-content-sm-padding-left: 3.25rem
}

.timeline-step:after {
    top: var(--mdb-timeline-step-top);
    height: var(--mdb-timeline-step-height)
}

.timeline-content {
    padding-left: var(--mdb-timeline-content-padding-left)
}

.timeline-head {
    padding-bottom: var(--mdb-timeline-head-padding-bottom)
}

.timeline-step-sm:after {
    left: var(--mdb-timeline-step-sm-left);
    height: 100%;
    top: var(--mdb-timeline-step-sm-top)
}

.timeline-head-sm {
    margin-right: var(--mdb-timeline-head-sm-margin-right);
    background-color: var(--mdb-timeline-head-sm-bg);
    border-radius: 100%;
    height: var(--mdb-timeline-head-sm-height);
    width: var(--mdb-timeline-head-sm-width)
}

.timeline-content-sm {
    padding-left: var(--mdb-timeline-content-sm-padding-left)
}

.select-dropdown .form-check-input label {
    display: block
}

select.select-initialized {
    display: none !important
}

.select-wrapper {
    --mdb-form-outline-select-arrow-color: var(--mdb-surface-color);
    --mdb-form-outline-select-arrow-font-size: 16px;
    --mdb-form-outline-select-arrow-top: 7px;
    --mdb-form-outline-select-arrow-right: 16px;
    --mdb-form-outline-select-valid-color: #00b74a;
    --mdb-form-outline-select-invalid-color: #f93154;
    --mdb-form-outline-select-clear-btn-color: var(--mdb-surface-color);
    --mdb-form-outline-select-clear-btn-font-size: 1rem;
    --mdb-form-outline-select-clear-btn-top: 7px;
    --mdb-form-outline-select-clear-btn-right: 27px;
    --mdb-form-outline-select-clear-btn-focus-color: #3b71ca;
    --mdb-form-outline-select-sm-clear-btn-font-size: 0.8rem;
    --mdb-form-outline-select-sm-clear-btn-top: 4px;
    --mdb-form-outline-select-lg-clear-btn-top: 11px;
    --mdb-form-outline-select-label-max-width: 80%;
    --mdb-form-outline-select-label-active-transform: translateY(-1rem) translateY(0.1rem) scale(0.8);
    --mdb-form-outline-select-lg-label-active-transform: translateY(-1.25rem) translateY(0.1rem) scale(0.8);
    --mdb-form-outline-select-sm-label-active-transform: translateY(-0.83rem) translateY(0.1rem) scale(0.8);
    --mdb-form-outline-select-input-focused-color: var(--mdb-surface-color);
    --mdb-form-outline-select-label-color: #3b71ca;
    --mdb-form-outline-select-notch-border-color: #3b71ca;
    --mdb-form-outline-select-white-notch-border-color: #fff;
    --mdb-form-outline-select-input-focused-arrow-color: #3b71ca;
    --mdb-form-outline-select-white-focus-arrow-color: #fff;
    --mdb-form-outline-select-white-arrow-color: #fff;
    --mdb-form-outline-select-white-clear-btn: #fff;
    --mdb-form-outline-select-sm-arrow-top: 3px;
    --mdb-form-outline-select-lg-arrow-top: 11px;
    --mdb-form-outline-form-notch-border-top: 1px solid transparent
}

.select-arrow {
    color: var(--mdb-form-outline-select-arrow-color);
    text-align: center;
    font-size: var(--mdb-form-outline-select-arrow-font-size);
    position: absolute;
    top: var(--mdb-form-outline-select-arrow-top);
    right: var(--mdb-form-outline-select-arrow-right)
}

.select-arrow::after {
    display: inline-block;
    margin-left: .255em;
    vertical-align: .255em;
    content: "";
    border-top: .3em solid;
    border-right: .3em solid rgba(0, 0, 0, 0);
    border-bottom: 0;
    border-left: .3em solid rgba(0, 0, 0, 0)
}

.select-arrow:empty::after {
    margin-left: 0
}

.was-validated .form-control:valid~.select-arrow {
    color: var(--mdb-form-outline-select-valid-color)
}

.was-validated .form-control:invalid~.select-arrow {
    color: var(--mdb-form-outline-select-invalid-color)
}

.select-clear-btn {
    color: var(--mdb-form-outline-select-clear-btn-color);
    font-size: var(--mdb-form-outline-select-clear-btn-font-size);
    position: absolute;
    top: var(--mdb-form-outline-select-clear-btn-top);
    right: var(--mdb-form-outline-select-clear-btn-right);
    cursor: pointer
}

.select-clear-btn:focus {
    color: var(--mdb-form-outline-select-clear-btn-focus-color);
    outline: none
}

.form-control-sm~.select-clear-btn {
    font-size: var(--mdb-form-outline-select-sm-clear-btn-font-size);
    top: var(--mdb-form-outline-select-sm-clear-btn-top)
}

.form-control-lg~.select-clear-btn {
    top: var(--mdb-form-outline-select-lg-clear-btn-top)
}

.select-dropdown-container {
    --mdb-form-outline-select-dropdown-container-z-index: 1070;
    --mdb-form-outline-select-dropdown-bg: var(--mdb-surface-bg);
    --mdb-form-outline-select-dropdown-box-shadow: 0 2px 5px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.16), 0 2px 10px 0 rgba(var(--mdb-box-shadow-color-rgb), 0.12);
    --mdb-form-outline-select-dropdown-min-width: 100px;
    --mdb-form-outline-select-dropdown-transform: scaleY(0.8);
    --mdb-form-outline-select-dropdown-transition: all 0.2s;
    --mdb-form-outline-select-dropdown-open-transform: scaleY(1);
    --mdb-form-outline-select-dropdown-input-group-padding: 10px;
    --mdb-form-outline-select-options-wrapper-scrollbar-width: 4px;
    --mdb-form-outline-select-options-wrapper-scrollbar-height: 4px;
    --mdb-form-outline-select-options-wrapper-scrollbar-border-bottom-right-radius: 4px;
    --mdb-form-outline-select-options-wrapper-scrollbar-border-bottom-left-radius: 4px;
    --mdb-form-outline-select-options-wrapper-scrollbar-thumb-height: 50px;
    --mdb-form-outline-select-options-wrapper-scrollbar-thumb-bg: var(--mdb-scrollbar-thumb-bg);
    --mdb-form-outline-select-options-wrapper-scrollbar-thumb-border-radius: 4px;
    --mdb-form-outline-select-no-results-padding-left: 16px;
    --mdb-form-outline-select-no-results-padding-right: 16px;
    z-index: var(--mdb-form-outline-select-dropdown-container-z-index)
}

.select-dropdown {
    background-color: var(--mdb-form-outline-select-dropdown-bg);
    box-shadow: var(--mdb-form-outline-select-dropdown-box-shadow);
    margin: 0;
    min-width: var(--mdb-form-outline-select-dropdown-min-width);
    outline: 0;
    position: relative;
    transform: var(--mdb-form-outline-select-dropdown-transform);
    opacity: 0;
    transition: var(--mdb-form-outline-select-dropdown-transition)
}

.select-dropdown.open {
    transform: var(--mdb-form-outline-select-dropdown-open-transform);
    opacity: 1
}

.select-dropdown>.input-group {
    padding: var(--mdb-form-outline-select-dropdown-input-group-padding)
}

.select-label {
    max-width: var(--mdb-form-outline-select-label-max-width);
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap
}

.select-label.active {
    transform: var(--mdb-form-outline-select-label-active-transform)
}

.form-control-lg~.select-label.active {
    transform: var(--mdb-form-outline-select-lg-label-active-transform)
}

.form-control-sm~.select-label.active {
    transform: var(--mdb-form-outline-select-sm-label-active-transform)
}

.form-outline .select-label.active~.form-notch .form-notch-middle {
    border-right: none;
    border-left: none;
    border-top: var(--mdb-form-outline-form-notch-border-top)
}

.select-input {
    cursor: pointer
}

.select-input[disabled] {
    cursor: default
}

.select-input.focused,
.form-outline .form-control.select-input:focus {
    color: var(--mdb-form-outline-select-input-focused-color);
    outline: 0
}

.select-input.focused~.select-label,
.form-outline .form-control.select-input:focus~.select-label {
    color: var(--mdb-form-outline-select-label-color)
}

.select-input.focused::placeholder,
.form-outline .form-control.select-input:focus::placeholder {
    opacity: 1
}

.select-input.focused~.form-notch .form-notch-leading,
.form-outline .form-control.select-input:focus~.form-notch .form-notch-leading {
    border-color: var(--mdb-form-outline-select-notch-border-color);
    box-shadow: -1px 0 0 0 var(--mdb-form-outline-select-notch-border-color), 0 1px 0 0 var(--mdb-form-outline-select-notch-border-color), 0 -1px 0 0 var(--mdb-form-outline-select-notch-border-color)
}

.select-input.focused~.form-notch .form-notch-trailing,
.form-outline .form-control.select-input:focus~.form-notch .form-notch-trailing {
    border-color: var(--mdb-form-outline-select-notch-border-color);
    box-shadow: 1px 0 0 0 var(--mdb-form-outline-select-notch-border-color), 0 -1px 0 0 var(--mdb-form-outline-select-notch-border-color), 0 1px 0 0 var(--mdb-form-outline-select-notch-border-color)
}

.select-input.focused~.form-notch .form-notch-middle {
    border-top: var(--mdb-form-outline-form-notch-border-top);
    border-color: var(--mdb-form-outline-select-notch-border-color);
    box-shadow: 0 1px 0 0 var(--mdb-form-outline-select-notch-border-color)
}

.select-input.focused~.select-arrow {
    color: var(--mdb-form-outline-select-input-focused-arrow-color)
}

.form-control-sm~.select-arrow {
    top: var(--mdb-form-outline-select-sm-arrow-top)
}

.form-control-lg~.select-arrow {
    top: var(--mdb-form-outline-select-lg-arrow-top)
}

.select-options-wrapper {
    overflow-y: auto
}

.select-options-wrapper::-webkit-scrollbar {
    width: var(--mdb-form-outline-select-options-wrapper-scrollbar-width);
    height: var(--mdb-form-outline-select-options-wrapper-scrollbar-height)
}

.select-options-wrapper::-webkit-scrollbar-button:start:decrement,
.select-options-wrapper::-webkit-scrollbar-button:end:increment {
    display: block;
    height: 0;
    background-color: rgba(0, 0, 0, 0)
}

.select-options-wrapper::-webkit-scrollbar-track-piece {
    background-color: rgba(0, 0, 0, 0);
    border-radius: 0;
    border-bottom-right-radius: var(--mdb-form-outline-select-options-wrapper-scrollbar-border-bottom-right-radius);
    border-bottom-left-radius: var(--mdb-form-outline-select-options-wrapper-scrollbar-border-bottom-left-radius)
}

.select-options-wrapper::-webkit-scrollbar-thumb:vertical {
    height: var(--mdb-form-outline-select-options-wrapper-scrollbar-thumb-height);
    background-color: var(--mdb-form-outline-select-options-wrapper-scrollbar-thumb-bg);
    border-radius: var(--mdb-form-outline-select-options-wrapper-scrollbar-thumb-border-radius)
}

.select-options-list {
    list-style: none;
    margin: 0;
    padding: 0
}

.select-option-group-label {
    --mdb-form-outline-select-option-group-label-padding-left: 16px;
    --mdb-form-outline-select-option-group-label-padding-right: 16px;
    --mdb-form-outline-select-option-group-label-font-size: 1rem;
    --mdb-form-outline-select-option-group-label-font-weight: 400;
    --mdb-form-outline-select-option-group-label-color: rgba(var(--mdb-emphasis-color-rgb), 0.55);
    width: 100%;
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding-left: var(--mdb-form-outline-select-option-group-label-padding-left);
    padding-right: var(--mdb-form-outline-select-option-group-label-padding-right);
    font-size: var(--mdb-form-outline-select-option-group-label-font-size);
    font-weight: var(--mdb-form-outline-select-option-group-label-font-weight);
    background-color: rgba(0, 0, 0, 0);
    color: var(--mdb-form-outline-select-option-group-label-color);
    user-select: none
}

.select-option-group>.select-option {
    --mdb-form-outline-select-option-group-select-option-padding-left: 26px;
    padding-left: var(--mdb-form-outline-select-option-group-select-option-padding-left)
}

.select-option {
    --mdb-form-outline-select-option-color: var(--mdb-surface-color);
    --mdb-form-outline-select-option-padding-left: 16px;
    --mdb-form-outline-select-option-padding-right: 16px;
    --mdb-form-outline-select-option-font-size: 1rem;
    --mdb-form-outline-select-option-font-weight: 400;
    --mdb-form-outline-select-option-hover-not-disabled-bg: var(--mdb-highlight-bg-color);
    --mdb-form-outline-select-option-active-bg: var(--mdb-highlight-bg-color);
    --mdb-form-outline-select-option-selected-active-bg: rgba(59, 113, 202, 0.45);
    --mdb-form-outline-select-option-selected-disabled-color: rgba(var(--mdb-surface-color-rgb), 0.5);
    --mdb-form-outline-select-option-disabled-color: rgba(var(--mdb-surface-color-rgb), 0.5);
    --mdb-form-outline-select-option-text-form-check-input-margin-right: 10px;
    --mdb-form-outline-select-option-secondary-text-font-size: 0.8rem;
    --mdb-form-outline-select-option-secondary-text-color: rgba(var(--mdb-emphasis-color-rgb), 0.55);
    --mdb-form-outline-select-option-icon-width: 28px;
    --mdb-form-outline-select-option-icon-height: 28px;
    --mdb-form-outline-select-white-arrow: #fff;
    --mdb-form-outline-select-option-disabled-secondary-text-color: rgba(var(--mdb-emphasis-color-rgb), 0.3);
    --mdb-form-outline-select-option-selected-bg: rgba(59, 113, 202, 0.3);
    --mdb-form-outline-select-option-selected-hover-bg: rgba(59, 113, 202, 0.45);
    width: 100%;
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
    cursor: pointer;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    color: var(--mdb-form-outline-select-option-color);
    padding-left: var(--mdb-form-outline-select-option-padding-left);
    padding-right: var(--mdb-form-outline-select-option-padding-right);
    font-size: var(--mdb-form-outline-select-option-font-size);
    font-weight: var(--mdb-form-outline-select-option-font-weight);
    background-color: rgba(0, 0, 0, 0);
    user-select: none
}

.select-option:hover:not(.disabled) {
    background-color: var(--mdb-form-outline-select-option-hover-not-disabled-bg)
}

.select-option.active {
    background-color: var(--mdb-form-outline-select-option-active-bg)
}

.select-option.selected.active {
    background-color: var(--mdb-form-outline-select-option-selected-active-bg)
}

.select-option.selected:hover:not(.disabled) {
    background-color: var(--mdb-form-outline-select-option-selected-hover-bg)
}

.select-option.selected {
    background-color: var(--mdb-form-outline-select-option-selected-bg)
}

.select-option.selected.disabled {
    cursor: default;
    color: var(--mdb-form-outline-select-option-selected-disabled-color);
    background-color: rgba(0, 0, 0, 0)
}

.select-option.disabled {
    cursor: default;
    color: var(--mdb-form-outline-select-option-disabled-color)
}

.select-option.disabled .select-option-secondary-text {
    color: var(--mdb-form-outline-select-option-disabled-secondary-text-color)
}

.select-option-text .form-check-input {
    margin-right: var(--mdb-form-outline-select-option-text-form-check-input-margin-right)
}

.select-option-secondary-text {
    font-size: var(--mdb-form-outline-select-option-secondary-text-font-size);
    color: var(--mdb-form-outline-select-option-secondary-text-color);
    display: block;
    line-height: normal
}

.select-option-icon {
    width: var(--mdb-form-outline-select-option-icon-width);
    height: var(--mdb-form-outline-select-option-icon-height)
}

.select-custom-content {
    --mdb-form-outline-select-custom-content-padding: 16px;
    padding: var(--mdb-form-outline-select-custom-content-padding)
}

.select-no-results {
    padding-left: var(--mdb-form-outline-select-no-results-padding-left);
    padding-right: var(--mdb-form-outline-select-no-results-padding-right);
    display: flex;
    align-items: center
}

.form-white .select-input.focused~.select-arrow {
    color: var(--mdb-form-outline-select-white-arrow-color)
}

.form-white .select-input:focus~.select-arrow {
    color: var(--mdb-form-outline-select-white-focus-arrow-color)
}

.form-white .select-arrow {
    color: var(--mdb-form-outline-select-white-arrow-color)
}

.form-white .select-clear-btn {
    color: var(--mdb-form-outline-select-white-clear-btn)
}

.form-white .select-input.focused,
.form-white .form-control.select-input:focus {
    color: #fff
}

.form-white .select-input.focused~.select-label,
.form-white .form-control.select-input:focus~.select-label {
    color: #fff
}

.form-white .select-input.focused~.form-notch .form-notch-leading,
.form-white .form-control.select-input:focus~.form-notch .form-notch-leading {
    border-color: var(--mdb-form-outline-select-white-notch-border-color);
    box-shadow: -1px 0 0 0 var(--mdb-form-outline-select-white-notch-border-color), 0 1px 0 0 var(--mdb-form-outline-select-white-notch-border-color), 0 -1px 0 0 var(--mdb-form-outline-select-white-notch-border-color)
}

.form-white .select-input.focused~.form-notch .form-notch-trailing,
.form-white .form-control.select-input:focus~.form-notch .form-notch-trailing {
    border-color: var(--mdb-form-outline-select-white-notch-border-color);
    box-shadow: 1px 0 0 0 var(--mdb-form-outline-select-white-notch-border-color), 0 -1px 0 0 var(--mdb-form-outline-select-white-notch-border-color), 0 1px 0 0 var(--mdb-form-outline-select-white-notch-border-color)
}

.form-outline .form-control~.form-label.select-fake-value,
.form-outline .form-control:focus~.form-label.select-fake-value,
.form-outline .form-control.active~.form-label.select-fake-value {
    transform: none;
    display: none
}

.form-outline .form-control~.form-label.select-fake-value.active,
.form-outline .form-control:focus~.form-label.select-fake-value.active,
.form-outline .form-control.active~.form-label.select-fake-value.active {
    display: block
}

code[class*=language-],
pre[class*=language-] {
    color: black;
    background: none;
    text-shadow: 0 1px white;
    font-family: Consolas, Monaco, "Andale Mono", "Ubuntu Mono", monospace;
    font-size: .875rem;
    text-align: left;
    white-space: pre;
    word-spacing: normal;
    word-break: normal;
    word-wrap: normal;
    line-height: 1.5;
    border-bottom-left-radius: .5rem;
    border-bottom-right-radius: .5rem;
    -moz-tab-size: 4;
    -o-tab-size: 4;
    tab-size: 4;
    -webkit-hyphens: none;
    -moz-hyphens: none;
    -ms-hyphens: none;
    hyphens: none
}

pre[class*=language-]::-moz-selection,
pre[class*=language-] ::-moz-selection,
code[class*=language-]::-moz-selection,
code[class*=language-] ::-moz-selection {
    text-shadow: none;
    background: #b3d4fc
}

pre[class*=language-]::selection,
pre[class*=language-] ::selection,
code[class*=language-]::selection,
code[class*=language-] ::selection {
    text-shadow: none;
    background: #b3d4fc
}

@media print {

    code[class*=language-],
    pre[class*=language-] {
        text-shadow: none
    }
}

pre[class*=language-] {
    padding: 1em;
    margin: .5em 0;
    overflow: auto
}

:not(pre)>code[class*=language-],
pre[class*=language-] {
    background: #f5f2f0
}

:not(pre)>code[class*=language-] {
    padding: .1em;
    border-radius: .3em;
    white-space: normal
}

.token.comment,
.token.prolog,
.token.doctype,
.token.cdata {
    color: slategray
}

.token.punctuation {
    color: #999
}

.namespace {
    opacity: .7
}

.token.property,
.token.tag,
.token.boolean,
.token.number,
.token.constant,
.token.symbol,
.token.deleted {
    color: #905
}

.token.selector,
.token.attr-name,
.token.string,
.token.char,
.token.builtin,
.token.inserted {
    color: #690
}

.token.operator,
.token.entity,
.token.url,
.language-css .token.string,
.style .token.string {
    color: #9a6e3a;
    background: hsla(0, 0%, 100%, 0.5)
}

.token.atrule,
.token.attr-value,
.token.keyword {
    color: #07a
}

.token.function,
.token.class-name {
    color: #dd4a68
}

.token.regex,
.token.important,
.token.variable {
    color: #e90
}

.token.important,
.token.bold {
    font-weight: bold
}

.token.italic {
    font-style: italic
}

.token.entity {
    cursor: help
}

pre.line-numbers {
    position: relative;
    padding-left: 3.8em;
    counter-reset: linenumber
}

pre.line-numbers>code {
    position: relative;
    white-space: inherit
}

.line-numbers .line-numbers-rows {
    position: absolute;
    pointer-events: none;
    top: 0;
    font-size: 100%;
    left: -3.8em;
    width: 3em;
    letter-spacing: -1px;
    border-right: 1px solid #999;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none
}

.line-numbers-rows>span {
    pointer-events: none;
    display: block;
    counter-increment: linenumber
}

.line-numbers-rows>span:before {
    content: counter(linenumber);
    color: #999;
    display: block;
    padding-right: .8em;
    text-align: right
}

.line-numbers .type-terminal .line-numbers-rows {
    border-right: none;
    top: -0.2em
}

.type-terminal .line-numbers-rows>span:before {
    content: "$"
}

.prism-previewer,
.prism-previewer:before,
.prism-previewer:after {
    position: absolute;
    pointer-events: none
}

.prism-previewer,
.prism-previewer:after {
    left: 50%
}

.prism-previewer {
    margin-top: -48px;
    width: 32px;
    height: 32px;
    margin-left: -16px;
    opacity: 0;
    -webkit-transition: opacity .25s;
    -o-transition: opacity .25s;
    transition: opacity .25s
}

.prism-previewer.flipped {
    margin-top: 0;
    margin-bottom: -48px
}

.prism-previewer:before,
.prism-previewer:after {
    content: "";
    position: absolute;
    pointer-events: none
}

.prism-previewer:before {
    top: -5px;
    right: -5px;
    left: -5px;
    bottom: -5px;
    border-radius: 10px;
    border: 5px solid #fff;
    box-shadow: 0 0 3px rgba(0, 0, 0, 0.5) inset, 0 0 10px rgba(0, 0, 0, 0.75)
}

.prism-previewer:after {
    top: 100%;
    width: 0;
    height: 0;
    margin: 5px 0 0 -7px;
    border: 7px solid transparent;
    border-color: rgba(255, 0, 0, 0);
    border-top-color: #fff
}

.prism-previewer.flipped:after {
    top: auto;
    bottom: 100%;
    margin-top: 0;
    margin-bottom: 5px;
    border-top-color: rgba(255, 0, 0, 0);
    border-bottom-color: #fff
}

.prism-previewer.active {
    opacity: 1
}

.prism-previewer-angle:before {
    border-radius: 50%;
    background: #fff
}

.prism-previewer-angle:after {
    margin-top: 4px
}

.prism-previewer-angle svg {
    width: 32px;
    height: 32px;
    -webkit-transform: rotate(-90deg);
    -moz-transform: rotate(-90deg);
    -ms-transform: rotate(-90deg);
    -o-transform: rotate(-90deg);
    transform: rotate(-90deg)
}

.prism-previewer-angle[data-negative] svg {
    -webkit-transform: scaleX(-1) rotate(-90deg);
    -moz-transform: scaleX(-1) rotate(-90deg);
    -ms-transform: scaleX(-1) rotate(-90deg);
    -o-transform: scaleX(-1) rotate(-90deg);
    transform: scaleX(-1) rotate(-90deg)
}

.prism-previewer-angle circle {
    fill: transparent;
    stroke: hsl(200, 10%, 20%);
    stroke-opacity: .9;
    stroke-width: 32;
    stroke-dasharray: 0, 500
}

.prism-previewer-gradient {
    background-image: linear-gradient(45deg, #bbb 25%, transparent 25%, transparent 75%, #bbb 75%, #bbb), linear-gradient(45deg, #bbb 25%, #eee 25%, #eee 75%, #bbb 75%, #bbb);
    background-size: 10px 10px;
    background-position: 0 0, 5px 5px;
    width: 64px;
    margin-left: -32px
}

.prism-previewer-gradient:before {
    content: none
}

.prism-previewer-gradient div {
    position: absolute;
    top: -5px;
    left: -5px;
    right: -5px;
    bottom: -5px;
    border-radius: 10px;
    border: 5px solid #fff;
    box-shadow: 0 0 3px rgba(0, 0, 0, 0.5) inset, 0 0 10px rgba(0, 0, 0, 0.75)
}

.prism-previewer-color {
    background-image: linear-gradient(45deg, #bbb 25%, transparent 25%, transparent 75%, #bbb 75%, #bbb), linear-gradient(45deg, #bbb 25%, #eee 25%, #eee 75%, #bbb 75%, #bbb);
    background-size: 10px 10px;
    background-position: 0 0, 5px 5px
}

.prism-previewer-color:before {
    background-color: inherit;
    background-clip: padding-box
}

.prism-previewer-easing {
    margin-top: -76px;
    margin-left: -30px;
    width: 60px;
    height: 60px;
    background: #333
}

.prism-previewer-easing.flipped {
    margin-bottom: -116px
}

.prism-previewer-easing svg {
    width: 60px;
    height: 60px
}

.prism-previewer-easing circle {
    fill: hsl(200, 10%, 20%);
    stroke: white
}

.prism-previewer-easing path {
    fill: none;
    stroke: white;
    stroke-linecap: round;
    stroke-width: 4
}

.prism-previewer-easing line {
    stroke: white;
    stroke-opacity: .5;
    stroke-width: 2
}

@-webkit-keyframes prism-previewer-time {
    0% {
        stroke-dasharray: 0, 500;
        stroke-dashoffset: 0
    }

    50% {
        stroke-dasharray: 100, 500;
        stroke-dashoffset: 0
    }

    100% {
        stroke-dasharray: 0, 500;
        stroke-dashoffset: -100
    }
}

@-o-keyframes prism-previewer-time {
    0% {
        stroke-dasharray: 0, 500;
        stroke-dashoffset: 0
    }

    50% {
        stroke-dasharray: 100, 500;
        stroke-dashoffset: 0
    }

    100% {
        stroke-dasharray: 0, 500;
        stroke-dashoffset: -100
    }
}

@-moz-keyframes prism-previewer-time {
    0% {
        stroke-dasharray: 0, 500;
        stroke-dashoffset: 0
    }

    50% {
        stroke-dasharray: 100, 500;
        stroke-dashoffset: 0
    }

    100% {
        stroke-dasharray: 0, 500;
        stroke-dashoffset: -100
    }
}

@keyframes prism-previewer-time {
    0% {
        stroke-dasharray: 0, 500;
        stroke-dashoffset: 0
    }

    50% {
        stroke-dasharray: 100, 500;
        stroke-dashoffset: 0
    }

    100% {
        stroke-dasharray: 0, 500;
        stroke-dashoffset: -100
    }
}

.prism-previewer-time:before {
    border-radius: 50%;
    background: #fff
}

.prism-previewer-time:after {
    margin-top: 4px
}

.prism-previewer-time svg {
    width: 32px;
    height: 32px;
    -webkit-transform: rotate(-90deg);
    -moz-transform: rotate(-90deg);
    -ms-transform: rotate(-90deg);
    -o-transform: rotate(-90deg);
    transform: rotate(-90deg)
}

.prism-previewer-time circle {
    fill: transparent;
    stroke: hsl(200, 10%, 20%);
    stroke-opacity: .9;
    stroke-width: 32;
    stroke-dasharray: 0, 500;
    stroke-dashoffset: 0;
    -webkit-animation: prism-previewer-time linear infinite 3s;
    -moz-animation: prism-previewer-time linear infinite 3s;
    -o-animation: prism-previewer-time linear infinite 3s;
    animation: prism-previewer-time linear infinite 3s
}

.docs-pills .d-flex.justify-content-between {
    border-bottom: 1px solid #e0e0e0 !important
}

.docs-pills .nav {
    border-bottom: 0 !important
}

.docs-pills .btn.btn-sm[class*=btn-outline-],
.docs-pills .btn-group-sm>.btn[class*=btn-outline-] {
    margin-top: .1rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important
}

.docs-pills .nav-pills .nav-link {
    padding: 10px 20px;
    margin: 0 5px
}

.docs-pills .tab-content {
    padding: 0
}

.docs-pills .btn-copy-code,
.btn-copy-code,
.docs-pills .export-to-snippet {
    position: absolute;
    top: 10px;
    right: 16px;
    font-size: .75rem;
    font-weight: 500
}

.docs-pills {
    position: relative !important
}

.docs-pills pre[class*=language-] {
    margin-top: 0;
    border: 1px solid #e0e0e0
}

pre.line-numbers {
    position: relative;
    padding-left: 3.8em !important;
    counter-reset: linenumber
}

pre.line-numbers>code {
    position: relative;
    white-space: inherit
}

.line-numbers .line-numbers-rows {
    position: absolute;
    pointer-events: none;
    top: 0;
    font-size: 100%;
    left: -3.8em;
    width: 3em;
    letter-spacing: -1px;
    border-right: 1px solid #999;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none
}

.line-numbers-rows>span {
    pointer-events: none;
    display: block;
    counter-increment: linenumber
}

.line-numbers-rows>span:before {
    content: counter(linenumber);
    color: #999;
    display: block;
    padding-right: .8em;
    text-align: right
}

.code-toolbar {
    margin: 0
}

code[class*=language-],
pre[class*=language-] {
    max-height: 450px
}

[data-mdb-theme=dark] .docs-pills .d-flex.justify-content-between {
    border-bottom: 1px solid #686868 !important
}

[data-mdb-theme=dark] code[class*=language-],
[data-mdb-theme=dark] pre[class*=language-] {
    color: white;
    text-shadow: none;
    background: #202022
}

[data-mdb-theme=dark] .docs-pills pre[class*=language-] {
    border: 1px solid #525252
}

[data-mdb-theme=dark] .token.operator,
[data-mdb-theme=dark] .token.entity,
[data-mdb-theme=dark] .token.url,
.language-css [data-mdb-theme=dark] .token.string,
[data-mdb-theme=dark] .style .token.string {
    color: #c6e0e0;
    background: transparent
}

[data-mdb-theme=dark] .token.attr-name,
[data-mdb-theme=dark] .token.char,
[data-mdb-theme=dark] .token.builtin,
[data-mdb-theme=dark] .token.inserted {
    color: rgb(220, 220, 220)
}

[data-mdb-theme=dark] .token.selector,
[data-mdb-theme=dark] .token.string {
    color: #73a3e6
}

[data-mdb-theme=dark] .token.function,
[data-mdb-theme=dark] .token.class-name {
    color: #b06edc
}

[data-mdb-theme=dark] .token.property,
[data-mdb-theme=dark] .token.tag,
[data-mdb-theme=dark] .token.boolean,
[data-mdb-theme=dark] .token.number,
[data-mdb-theme=dark] .token.constant,
[data-mdb-theme=dark] .token.symbol,
[data-mdb-theme=dark] .token.deleted {
    color: #dc6eaf
}

[data-mdb-theme=dark] .token.atrule,
[data-mdb-theme=dark] .token.attr-value,
[data-mdb-theme=dark] .token.keyword {
    color: #73c8e6
}

[data-mdb-theme=dark] .token.comment {
    color: #999
}

[data-mdb-theme=dark] .code-toolbar pre::-webkit-scrollbar {
    width: 15px
}

[data-mdb-theme=dark] .code-toolbar pre::-webkit-scrollbar-track {
    background-color: #272626 !important
}

[data-mdb-theme=dark] .code-toolbar pre::-webkit-scrollbar-thumb {
    background-color: #444242 !important;
    border-radius: 2px
}

[data-mdb-theme=dark] .code-toolbar pre::-webkit-scrollbar-corner {
    background-color: #272626 !important
}

#mdb-footer {
    padding-left: 240px
}

@media(max-width: 1439px) {
    #mdb-footer {
        padding-left: 0
    }
}

#mdb-intro {
    padding-left: 240px;
    margin-top: 58.51px
}

@media(max-width: 1439px) {
    #mdb-intro {
        padding-left: 0
    }
}
"""

# List of classes to search for
words = ['body','col-lg-7', 'col-lg-5', 'd-flex', 'justify-content-between', 'small', 'mb-0', 
         'text-muted', 'h-100', 'h-custom', 'fas', 'fa-trash-alt', 'container', 'py-5', 'text-body', 
         'fab fa-cc-amex',  'me-2', 'mb-1', 'align-items-center', 'mb-4', 'fa-cc-mastercard ','fa-2x', 
         'mb-2', 'mb-3', 'card-body', ' fa-cc-paypal','flex-row ', 'card',  'mb-lg-0',  
         'fa-long-arrow-alt-left', ' bg-primary', 'text-white', ' fa-angle-down', 'mt-1', 
         'txt', 'fw-normal', 'p-4', 'my-4', 'center', 'fa-cc-visa ', 'fa-long-arrow-alt-right',
         'ms-2', 'btn', 'btn-info', 'btn-block', 'btn-lg', 'row', 'img-fluid', 'rounded-3', 'ms-3']

# Extract CSS code for the specified classes
class_css_dict = extract_css_for_classes(css_code, words)

# Print the extracted CSS code for each class
for class_name, class_code in class_css_dict.items():
    print(f"Class: {class_name}")
    print(f"Code: {class_code}\n")
