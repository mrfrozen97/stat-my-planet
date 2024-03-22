const superagent = require("superagent").agent();

function addNewRow(){
    const newRow = document.createElement("div");
    newRow.classList.add("country-row");
    document.getElementById("countires-box").appendChild(newRow);
}

const ytm = async (url) => {
    let dashboard = await superagent.get(url)
    .send()

    console.log("abc");
    console.log(dashboard.text);
} 


addNewRow();
addNewRow();
addNewRow();



ytm("https://www.usdebtclock.org/world-debt-clock.html");