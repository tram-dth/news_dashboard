const country = document.getElementById("country-selector");
const category = document.getElementById("category-selector");
const user_input_prompt = document.getElementById("user-input-prompt")
const go_button = document.getElementById("go-button")

function text_prompt() {
    let country_str = country.value.trim();
    let category_str = category.value.trim();
    if (country_str === "") {
        user_input_prompt.textContent = "Please select a country and a news category"
    } else if (category_str === "") {
        user_input_prompt.textContent = "Please select a news category"
    } else {
        user_input_prompt.textContent = "PRESS GO!!!"
    }
}


function process_request() {
    let country_str = country.value.trim();
    let category_str = category.value.trim();
    if ((country_str === "")||(category_str === "")) {
        user_input_prompt.textContent = "Please input both country and news categories"
    } else {
        
    }
}



country.addEventListener("change", text_prompt);
category.addEventListener("change", text_prompt);
go_button.addEventListener("click", process_request)


