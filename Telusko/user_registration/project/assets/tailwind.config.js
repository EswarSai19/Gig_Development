/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../**/templates/**/*.html", // All HTML files in the templates directory of all apps
    "../**/static/js/**/*.js", // Any JavaScript files
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
