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
    { name: "Belgium (België)", code: "+32", flag: "be" },
    { name: "Brazil (Brasil)", code: "+55", flag: "br" },
    { name: "Bulgaria (България)", code: "+359", flag: "bg" },
    { name: "Canada", code: "+1", flag: "ca" },
    { name: "China (中国)", code: "+86", flag: "cn" },
    { name: "Colombia", code: "+57", flag: "co" },
    { name: "Denmark (Danmark)", code: "+45", flag: "dk" },
    { name: "Egypt (مصر)", code: "+20", flag: "eg" },
    { name: "Finland (Suomi)", code: "+358", flag: "fi" },
    { name: "France", code: "+33", flag: "fr" },
    { name: "Germany (Deutschland)", code: "+49", flag: "de" },
    { name: "Greece (Ελλάδα)", code: "+30", flag: "gr" },
    { name: "India (भारत)", code: "+91", flag: "in" },
    { name: "Indonesia", code: "+62", flag: "id" },
    { name: "Iran (ایران)", code: "+98", flag: "ir" },
    { name: "Iraq (العراق)", code: "+964", flag: "iq" },
    { name: "Ireland (Éire)", code: "+353", flag: "ie" },
    { name: "Israel (ישראל)", code: "+972", flag: "il" },
    { name: "Italy (Italia)", code: "+39", flag: "it" },
    { name: "Japan (日本)", code: "+81", flag: "jp" },
    { name: "Kazakhstan (Қазақстан)", code: "+7", flag: "kz" },
    { name: "Kyrgyzstan (Кыргызстан)", code: "+996", flag: "kg" },
    { name: "Malaysia", code: "+60", flag: "my" },
    { name: "Mexico (México)", code: "+52", flag: "mx" },
    { name: "Morocco (المغرب)", code: "+212", flag: "ma" },
    { name: "Netherlands (Nederland)", code: "+31", flag: "nl" },
    { name: "New Zealand", code: "+64", flag: "nz" },
    { name: "Norway (Norge)", code: "+47", flag: "no" },
    { name: "Pakistan (پاکستان)", code: "+92", flag: "pk" },
    { name: "Philippines", code: "+63", flag: "ph" },
    { name: "Poland (Polska)", code: "+48", flag: "pl" },
    { name: "Portugal", code: "+351", flag: "pt" },
    { name: "Qatar (قطر)", code: "+974", flag: "qa" },
    { name: "Romania (România)", code: "+40", flag: "ro" },
    { name: "Russia (Россия)", code: "+7", flag: "ru" },
    { name: "Saudi Arabia (السعودية)", code: "+966", flag: "sa" },
    { name: "South Africa", code: "+27", flag: "za" },
    { name: "South Korea (대한민국)", code: "+82", flag: "kr" },
    { name: "Spain (España)", code: "+34", flag: "es" },
    { name: "Sweden (Sverige)", code: "+46", flag: "se" },
    { name: "Switzerland (Schweiz)", code: "+41", flag: "ch" },
    { name: "Syria (سوريا)", code: "+963", flag: "sy" },
    { name: "Tajikistan (Тоҷикистон)", code: "+992", flag: "tj" },
    { name: "Thailand (ประเทศไทย)", code: "+66", flag: "th" },
    { name: "Turkey (Türkiye)", code: "+90", flag: "tr" },
    { name: "Turkmenistan (Türkmenistan)", code: "+993", flag: "tm" },
    { name: "Ukraine (Україна)", code: "+380", flag: "ua" },
    { name: "United Arab Emirates (الإمارات)", code: "+971", flag: "ae" },
    { name: "United Kingdom", code: "+44", flag: "gb" },
    { name: "United States", code: "+1", flag: "us" },
    { name: "Uzbekistan (O'zbekiston)", code: "+998", flag: "uz" },
    { name: "Vietnam (Việt Nam)", code: "+84", flag: "vn" },
    { name: "Yemen (اليمن)", code: "+967", flag: "ye" }
];