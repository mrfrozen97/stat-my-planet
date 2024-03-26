//const superagent = require("superagent").agent();
//const serverName = "https://mrfrozen97.github.io/stat-my-planet/";
const serverName = "http://127.0.0.1:5500/";

function addCountryNameBlock(row, data){
    console.log(data);
    const nameBlock = document.createElement("div");
    nameBlock.classList.add("country-name-block");
    const countryText = document.createElement("h4");
    countryText.innerHTML = data["country_name"];
    countryText.classList.add("country-name-block-title");
    const img = document.createElement("img");
    img.classList.add("flag-icon");
    img.setAttribute("src", "resources\\flags\\" + data["country_name"] + ".png");
    nameBlock.appendChild(img);
    nameBlock.appendChild(countryText);
    row.appendChild(nameBlock);
}

function reverseString(str) {

    // empty string
    let newString = "";
    for (let i = str.length - 1; i >= 0; i--) {
        newString += str[i];
    }
    return newString;
}

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function formatMoney(num){
    if(num == "GDP" || num == "Total Debt"){return num;}
    return "$" + numberWithCommas(num);
}

function calculateLiveGdp(country, base_gdp, percent){
    if(base_gdp == "GDP"){
        return base_gdp;
    }
    let currTime = Math.floor((new Date()).getTime() / 1000);
    let newYearTime = Math.floor((new Date(new Date().getFullYear(), 0, 1)).getTime() / 1000);
    let gdp = Math.floor(base_gdp + base_gdp*((currTime-newYearTime)/(365*24*3600) * (percent/100)));
    //console.log(country);
    return gdp;
}

function calculateLiveDebt(liveGDP, debtRatio){
    if(debtRatio != undefined){
        let liveDebt = Math.floor(liveGDP * (debtRatio/100));
        return liveDebt;
    }
    return "Total Debt";
}

function addCountryGDPBlock(row, data){
    const gdpBlock = document.createElement("div");
    gdpBlock.classList.add("country-data-block");
    gdpBlock.classList.add("country-data-block-gdp");
    let countryData = data[row.childNodes[0].childNodes[1].innerHTML];
    if(countryData == undefined){
        return "No Data";
    }
    gdpBlock.innerHTML = countryData["gdp"];
    //row.appendChild(gdpBlock);
    //calculateLiveGdp( data[row.childNodes[0].childNodes[1].innerHTML]["gdp"], 4);
    row.insertBefore(gdpBlock, row.childNodes[1]);
}

function UpdateCountryDataBlock(row, data){

    let liveGdp = calculateLiveGdp( row.childNodes[0].childNodes[1].innerHTML,
        data[row.childNodes[0].childNodes[1].innerHTML]["gdp"],
        data[row.childNodes[0].childNodes[1].innerHTML]["percent"]);
    row.childNodes[1].innerHTML =  formatMoney(liveGdp);
    row.childNodes[2].innerHTML = formatMoney(calculateLiveDebt(liveGdp,
        data[row.childNodes[0].childNodes[1].innerHTML]["debt_ratio"]));
    //row.appendChild(gdpBlock);
   ;
    
}


function addCountryDebtBlock(row, data){
    const debtBlock = document.createElement("div");
    debtBlock.classList.add("country-data-block");
    debtBlock.classList.add("country-data-block-debt");
    let countryData = data[row.childNodes[0].childNodes[1].innerHTML];
    if(countryData == undefined){
        debtBlock.innerHTML = "No Data";
    }
    else{
        debtBlock.innerHTML = countryData["popularion"];
    }
    row.insertBefore(debtBlock, row.childNodes[3]);
    row.appendChild(debtBlock);
}

function addCountryPopulationBlock(row, data){
    const debtBlock = document.createElement("div");
    debtBlock.classList.add("country-data-block");
    let countryData = data[row.childNodes[0].childNodes[1].innerHTML];
    if(countryData["population"] == undefined){
        debtBlock.innerHTML = "No Data";
    }
    else{
        debtBlock.innerHTML = countryData["population"];
    }
    row.insertBefore(debtBlock, row.childNodes[3]);
    
}

function addCountryDgRatioBlock(row, data){
    const ratioBlock = document.createElement("div");
    ratioBlock.classList.add("country-data-block");
    ratioBlock.classList.add("country-data-block-ratio");
    if(data["dg_ratio"] == undefined){
        ratioBlock.innerHTML = "No Data";
    }
    else{
        ratioBlock.innerHTML = data["dg_ratio"]+"%";
    }
    row.appendChild(ratioBlock);
}

function addCountryBlocks(row, data){

    addCountryNameBlock(row, data);
    //addCountryGDPBlock(row, data);
    addCountryDebtBlock(row, data);
    //addCountryPopulationBlock(row, data);
    addCountryDgRatioBlock(row, data);
      
}

function addNewRow(data){
    const newRow = document.createElement("div");
    newRow.setAttribute("id", data["country_name"]);
    newRow.classList.add("country-row");
    document.getElementById("countires-box").appendChild(newRow);
    addCountryBlocks(newRow, data);
}


fetch((serverName+"/data/country_all.json"))
.then((response) => response.json())
.then( (json)=>{
    for(let i = 0; i<json["country_data"].length; i++){
        var countriesEconomicsData = json["country_data"][i];
        console.log(countriesEconomicsData);
        addNewRow(countriesEconomicsData);
    
    }

});

fetch((serverName+"/data/country_gdp.json"))
.then((response) => response.json())
.then( (json)=>{

    let rows = document.querySelectorAll(".country-row");
    console.log(rows);
    for(let i=0; i<rows.length; i++){
        addCountryGDPBlock(rows[i], json);
        addCountryPopulationBlock(rows[i], json);
    }

    setInterval(() =>{
        
        for(let i=0; i<rows.length; i++){
            UpdateCountryDataBlock(rows[i], json);
        }
        
    }, 500);

});
