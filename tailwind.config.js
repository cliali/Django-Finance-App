/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./finance_config/tracker/templates/**/*.html",
    "./config/templates/**/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('daisyui'),
  ],
}
