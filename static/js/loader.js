function showLoader() {
    $("div.loading-container").removeClass("hide-overlay").addClass("overlay");
}
function hideLoader() {
    $("div.loading-container").removeClass("overlay").addClass("hide-overlay");
}
const serverOrigin = "http://localhost:8000"

let queryParams = {}
function getParams(){
    queryParams = {}
    const url = new URL(window.location.href);
    const params = new URLSearchParams(url.search);
    queryParams = params
    
}