/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // Include all your template files
    "./**/templates/**/*.html", // Include app-specific templates
    "./non_register/templates/**/*.html", // Include app-specific templates
    "./freelancer/templates/**/*.html", // Include app-specific templates
    "./client/templates/**/*.html", // Include app-specific templates
    "./myadmin/templates/**/*.html", // Include app-specific templates
  ],
  theme: {
    extend: {
      fontFamily: {
        arial: ["Arial", "sans-serif"],
      },
      colors: {
        cl_nav_hover: "#3dd9d6",
      },
    },
  },
  plugins: [],
};
