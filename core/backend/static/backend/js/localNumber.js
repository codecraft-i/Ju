const countries = [
    { name: "Afghanistan (افغانستان)", code: "+93", flag: "af" },
    { name: "Albania (Shqipëri)", code: "+355", flag: "al" },
    { name: "Algeria (الجزائر)", code: "+213", flag: "dz" },
    { name: "Andorra", code: "+376", flag: "ad" },
    { name: "Angola", code: "+244", flag: "ao" },
    { name: "Argentina", code: "+54", flag: "ar" },
    { name: "Armenia (Հայաստան)", code: "+374", flag: "am" },
    { name: "Australia", code: "+61", flag: "au" },
    { name: "Austria (Österreich)", code: "+43", flag: "at" },
    { name: "Azerbaijan (Azərbaycan)", code: "+994", flag: "az" },
    { name: "Bahrain (البحرين)", code: "+973", flag: "bh" },
    { name: "Bangladesh (বাংলাদেশ)", code: "+880", flag: "bd" },
    { name: "Belarus (Беларусь)", code: "+375", flag: "by" },
    { name: "Ukraine (Україна)", code: "+380", flag: "ua" },
    { name: "United Arab Emirates (الإمارات)", code: "+971", flag: "ae" },
    { name: "United Kingdom", code: "+44", flag: "gb" },
    { name: "United States", code: "+1", flag: "us" },
    { name: "Uzbekistan (O'zbekiston)", code: "+998", flag: "uz" },
    { name: "Vietnam (Việt Nam)", code: "+84", flag: "vn" },
    { name: "Yemen (اليمن)", code: "+967", flag: "ye" }
];

let selectedCountryLength = null;

function toggleDropdown() {
    const list = document.getElementById("countryList");
    list.style.display = list.style.display === "block" ? "none" : "block";
    event.stopPropagation();
}

function selectCountry(code, flag, length) {
    document.getElementById("code").innerText = code;
    document.getElementById("flag").src = `https://flagcdn.com/w40/${flag}.png`;
    document.getElementById("countryList").style.display = "none";
    selectedCountryLength = code === "+998" ? 9 : length;
    updateFullPhone();
}

window.onload = function() {
    const list = document.getElementById("countryList");
    countries.forEach(country => {
        let div = document.createElement("div");
        div.innerHTML = `<span class="country-name">${country.name}</span> <span>${country.code}</span> <img src="https://flagcdn.com/w40/${country.flag}.png" class="flag" style="margin-left: 5px;">`;
        div.onclick = () => selectCountry(country.code, country.flag, country.length);
        list.appendChild(div);
    });
}

function updateFullPhone() {
    const countryCode = document.getElementById("code").innerText.trim();
    const phoneNumber = document.getElementById("phone").value.trim().replace(/\s/g, '');
    const fullPhone = countryCode + phoneNumber;
    document.getElementById("fullPhone").value = fullPhone;

    let errorDiv = document.getElementById("submitError");
    if (!errorDiv) {
        errorDiv = document.createElement("div");
        errorDiv.id = "submitError";
        errorDiv.style.color = "red";
        document.getElementById("phone").parentNode.appendChild(errorDiv);
    }

    let submitErrorDiv = document.getElementById("submitError");
    if (!submitErrorDiv) {
        submitErrorDiv = document.createElement("div");
        submitErrorDiv.id = "submitError";
        submitErrorDiv.style.color = "red";
        submitErrorDiv.style.marginTop = "10px";
        document.getElementById("registrationForm").appendChild(submitErrorDiv);
    }

    if (countryCode === "+998") {
        if (phoneNumber.length > 9) {
            document.getElementById("phone").value = phoneNumber.slice(0, 9);
            errorDiv.innerText = "Telefon raqami 9 raqamdan iborat bo‘lishi kerak!";
        } else if (phoneNumber.length < 9 && phoneNumber.length > 0) {
            errorDiv.innerText = "Telefon raqami 9 raqamdan iborat bo‘lishi kerak!";
        } else {
            errorDiv.innerText = "";
        }
    } else {
        if (phoneNumber.length > 20) {
            document.getElementById("phone").value = phoneNumber.slice(0, 20);
            errorDiv.innerText = "Telefon raqami 20 raqamdan oshmasligi kerak!";
        } else if (phoneNumber.length < 1 && phoneNumber.length > 0) {
            errorDiv.innerText = "Telefon raqami kamida 1 raqamdan iborat bo‘lishi kerak!";
        } else {
            errorDiv.innerText = "";
        }
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const phoneInput = document.getElementById("phone");
    phoneInput.addEventListener("input", function() {
        this.value = this.value.replace(/[^0-9]/g, '');
        updateFullPhone();
    });

    document.addEventListener("click", function(event) {
        const countryList = document.getElementById("countryList");
        if (countryList.style.display === "block") {
            countryList.style.display = "none";
        }
    });

    document.getElementById("registrationForm").addEventListener("submit", function (event) {
        updateFullPhone();
        const phoneNumber = document.getElementById("phone").value.trim().replace(/\s/g, '');
        const countryCode = document.getElementById("code").innerText.trim();
        const submitErrorDiv = document.getElementById("submitError");

        if (countryCode === "+998" && phoneNumber.length !== 9) {
            event.preventDefault();
            submitErrorDiv.innerText = "Telefon raqami 9 raqamdan iborat bo‘lishi kerak!";
            return;
        } else if (countryCode !== "+998" && (phoneNumber.length < 1 || phoneNumber.length > 20)) {
            event.preventDefault();
            submitErrorDiv.innerText = "Telefon raqami 1 dan 20 gacha raqamdan iborat bo‘lishi kerak!";
            return;
        } else {
            submitErrorDiv.innerText = "";
        }

        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]');
        if (!csrfToken || csrfToken.value === "") {
            event.preventDefault();
            submitErrorDiv.innerText = "Xatolik: CSRF token topilmadi!";
        }
    });
});