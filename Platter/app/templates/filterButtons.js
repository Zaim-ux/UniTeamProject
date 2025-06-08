$(document).ready(function() {
    // Initial state of filters
    var dairyActive = false;
    var nutsActive = false;
    var glutenActive = false;
    var vegetarianActive = false;
    var spicelessActive = false;
    var mildActive = false;
    var hotActive = false;
    var veryHotActive = false;
    var startersActive = false;
    var mainsActive = false;
    var dessertActive = false;
    var drinksActive = false;


    // Function to update the URL based on filter states
    function updateURL() {
        var url = '/filtered_menu_items/?';
        if (dairyActive) {
            url += 'allergy=dairy&';
        }
        if (nutsActive) {
            url += 'allergy=nuts&';
        }
        if (glutenActive) {
            url += 'allergy=gluten&';
        }
        if (vegetarianActive) {
            url += 'allergy=vegetarian&';
        }
        if (spicelessActive) {
            url += 'spice=spiceless&';
        }
        if (mildActive) {
            url += 'spice=mild&';
        }
        if (hotActive) {
            url += 'spice=hot&';
        }
        if (veryHotActive) {
            url += 'spice=veryHot&';
        }
        if (startersActive) {
            url += 'category=starters&';
        }
        if (mainsActive) {
            url += 'category=mains&';
        }
        if (dessertActive) {
            url += 'category=dessert&';
        }
        if (drinksActive) {
            url += 'category=drinks&';
        }

        window.history.pushState({}, '', url.slice(0, -1));  // Remove trailing '&' and adds the url string to url 
    }

    // button toggles
    $('#dairyToggle').click(function() {
        dairyActive = !dairyActive;
        updateURL();
    });
    
    $('#nutsToggle').click(function() {
        nutsActive = !nutsActive;
        updateURL();
    });
    
    $('#glutenToggle').click(function() {
        glutenActive = !glutenActive;
        updateURL();
    });

    $('#vegetarianToggle').click(function() {
        vegetarianActive = !vegetarianActive;
        updateURL();
    });

    $('spicelessToggle').click(function() {
        spicelessctive = !spicelessActive;
        updateURL();
    });

    $('#mildToggle').click(function() {
        mildActive = !mildActive;
        updateURL();
    });

    $('#hotToggle').click(function() {
        hotyActive = !hotActive;
        updateURL();
    });

    $('#veryHotToggle').click(function() {
        veryHotActive = !veryHotActive;
        updateURL();
    });

    $('#startersToggle').click(function() {
        startersActive = !startersActive;
        updateURL();
    });

    $('#mainsToggle').click(function() {
        mainsActive = !mainsActive;
        updateURL();
    });

    $('#dessertToggle').click(function() {
        dessertActive = !dessertActive;
        updateURL();
    });

    $('#drinksToggle').click(function() {
        drinksActive = !drinksActive;
        updateURL();
    });


});