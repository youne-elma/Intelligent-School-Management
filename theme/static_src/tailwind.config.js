/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
  content: [
    /**
     * HTML. Paths to Django template files that will contain Tailwind CSS classes.
     */

    /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
    "../templates/**/*.html",

    /*
     * Main templates directory of the project (BASE_DIR/templates).
     * Adjust the following line to match your project structure.
     */
    "../../templates/**/*.html",

    /*
     * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
     * Adjust the following line to match your project structure.
     */
    "../../**/templates/**/*.html",

    /**
     * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
     * patterns match your project structure.
     */
    /* JS 1: Ignore any JavaScript in node_modules folder. */
    // '!../../**/node_modules',
    /* JS 2: Process all JavaScript files in the project. */
    // '../../**/*.js',

    /**
     * Python: If you use Tailwind CSS classes in Python, uncomment the following line
     * and make sure the pattern below matches your project structure.
     */
    // '../../**/*.py'
  ],
  theme: {
    extend: {},
    fontFamily: {
      poppin: ["Poppins"],
      poppinRegular: ["PoppinsRegular"],
      poppinSemiBold: ["PoppinsMedium"],
      poppinMedium: ["PoppinsMedium"],
    },
    variants:{
      extend: {
        display:['group-focus']
      },
    },
    colors: {
      lightcolor: "#F1F1F1",
      darkcolor: "#202020",
      mediumcoolGray: "#7E909A",
      loyalblue: "#1C4E80",
      lightblue: "#A5D8DD",
      daredvilleorange: "#EA6A47",
      denimcolor: "#0091D5",
      cornflower: "#1C4E80",
      smoothgreen: "#618830",
      bluecharcoal: "#22282E",
      buttonhover: "#1C4E80",
      testColor: "#3b82f6",
      skybleau: "#e0f2fe",
      while1: "#f8fafc",
      whte2: "#f1f5f9",
      skybleu2: "#93c5fd",
      clearwhite: "#FFFFFF",
      slidebuttonimage: "#D9D9D9",
      slidebuttonimageactive: "#FFFFFF",
      lightgreen:"#0BAF74",
      white:"#FFFFFF",
      BroderGris:"#d9d9d985",
      gris:"#94a3b8",
      informationColor:"#7A7A7A",
    },
    screens: {
      navbarTab: { min: "1000px", max: "1200px" },
      navbarMinTab: { min: "760px", max: "1000px" },
      navbarPhone: { max: "760px" },
      navBarNotPhone: { min: "760px" },
      loginimagehide: { max: "770px" },
      AnnounceViewport: {max:"1000px"},
      'SmallScreen':{ min:"1px",max:'645px'},
      'md': {min:"645px",max:"1000px"},
      'xl':{min:"1000px",max:"1400px"},
      '2xl':{min:"1400px",max:"1777px"},
      '3xl':{min:"1777px", max:"2000px"},
      'Big':{min:"1777px"},
      ecoursScreen: { min:"500px", max: "1150px" },
      ecoursMScreen: {  max: "500px" },
      smScreen:{min:"1px",max:"300px"},
      chatonlywide: { min: "1000px" },
      chatonlytab: { min: "760px", max: "1000px" },
      chatonlyphone: { max: "760px" },
      chattextportable: { max: "1000px" },
      ajoutAnnonceBig: { min: "1300px", max: "1430px" },
      ajoutAnnonceTab: { max: "1300px" },
      ajoutAnnonceMobile: { max: "700px" },
    },
    boxShadow: {
      sm: "0px 4px 4px rgba(0, 0, 0, 0.25)",
      lm: "2px 2px 11px rgba(0, 0, 0, 0.25)",
      input: "1px 1px 20px rgba(0, 0, 0, 0.1)",
    },
    dropShadow: {
      sm: " 2px 2px 10px rgba(0, 0, 0, 0.08)",
    },
  },

  plugins: [
    /**
     * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
     * for forms. If you don't like it or have own styling for forms,
     * comment the line below to disable '@tailwindcss/forms'.
     */

    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/line-clamp"),
    require("@tailwindcss/aspect-ratio"),
    require("postcss-simple-vars"),
  ],
};


