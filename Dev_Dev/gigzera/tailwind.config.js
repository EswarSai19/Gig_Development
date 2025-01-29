/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // Include all your template files
    "./**/templates/**/*.html", // Include app-specific templates
    "./non_register/templates/**/*.html", // Include app-specific templates
    "./freelancer/templates/**/*.html", // Include app-specific templates
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
