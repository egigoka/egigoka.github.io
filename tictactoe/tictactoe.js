

var cnt = 0;
function helloWorld(){
    document.write("Hello World!");
    cnt++;
    document.body.innerHTML = "<button onclick=\"helloWorld()\">Oh hello</button>" + cnt;
}

function fillTable(data) {
    let table = document.querySelector("table");
    for (let element of data) {
        let row = table.insertRow();
        for (key in element) {
            let cell = row.insertCell();
            let text = document.createTextNode(element[key]);
            cell.appendChild(text);
        }
    }
}