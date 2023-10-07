const cityOpt = document.querySelector('.nvs-city');
const stateOpt = document.querySelector('.nvs-state');
const apitoken = "b19cbc72dd360d2378f7d76043e7f49a2de28012"


var apiUrl = 'http://172.25.45.100:8000/';
var xhr = new XMLHttpRequest();
xhr.open('GET', apiUrl, true);
xhr.setRequestHeader("Authorization", `token ${apitoken}`);
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.onload = function() {
    if (xhr.status === 200) {
        var data = JSON.parse(xhr.responseText);
        stateOpt.innerHTML = `<option selected >Choose...</option>`
        data.forEach((item) => {
            stateOpt.innerHTML +=`
            <option value='${item}'>${item}</option>`;
        });
        addcitynames()
    }
    };
xhr.send();


function addcitynames(){
    stateOpt.addEventListener('change', (e) => {
        const statevalue = e.target.value;
    
        if(statevalue.length > 0){
            var SendData = {
                state : statevalue,
            }
            var apiUrl = 'http://172.25.45.100:8000/';
            var xhr = new XMLHttpRequest();
            xhr.open('POST', apiUrl, true);
            xhr.setRequestHeader("Authorization", `token ${apitoken}`);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onload = function() {
                if (xhr.status === 200) {
                    var data = JSON.parse(xhr.responseText);
                    cityOpt.innerHTML = '';
                    if (data[0] === 'not_state'){
                        console.log('not',data)
                        cityOpt.innerHTML = `
                        <option selected >Please select state</option>`;
                    }else{
                        cityOpt.innerHTML = `
                        <option selected >Choose...</option>`;
                        data.forEach((item) => {
                            cityOpt.innerHTML +=`
                            <option value='${item}'>${item}</option>`;
                        });
                    }
                }
            };
            xhr.send(JSON.stringify(SendData));
        }
    });
}