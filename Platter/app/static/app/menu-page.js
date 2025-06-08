$(document).ready(function () {
    // Initial state of filters
    let queryParamsMapping = {
        dairy: {query: 'allergy=dairy&'},
        nuts: {query: 'allergy=nuts&'},
        gluten: {query: 'allergy=gluten&'},
        vegetarian: {query: 'allergy=vegetarian&'},
        mild: {query: 'spice=mild&'},
        hot: {query: 'spice=hot&'},
        atomic: {query: 'spice=atomic&'},
        starters: {query: 'category=starters&'},
        mains: {query: 'category=mains&'},
        dessert: {query: 'category=dessert&'},
        drinks: {query: 'category=drinks&'}
    };

    for (const key in queryParamsMapping) {
        queryParamsMapping[key] = {
            ...queryParamsMapping[key],
            state: false
        }
    }

    // Function to update the URL based on filter states
    function updateURL() {
        let url = '/app/filteredItems/?';
        for (let value in queryParamsMapping) {
            if (queryParamsMapping[value].state) {
                url += queryParamsMapping[value].query;
            }
        }
        window.history.pushState({}, '', url.slice(0, -1));  // Remove trailing '&' and adds the url string to url
        //location.reload(true);
    }

    //apply and clear filter buttons
    $('#applyF').click(function () {
        location.reload();
    });

    $('#clearF').click(function () {
        updateURL();
        location.reload();
    });

    // button toggles
    const toggles = ['dairy', 'nuts', 'gluten', 'vegetarian', 'mild', 'hot', 'atomic', 'starters', 'mains', 'dessert', 'drinks'];

    toggles.forEach(toggle => {
        $(`#${toggle}Toggle`).click(function () {
            queryParamsMapping[toggle].state = !queryParamsMapping[toggle].state;
            updateURL();
        });
    });
});

