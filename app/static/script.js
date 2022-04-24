function httpGet(url) {
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", url, false); // false for synchronous request
    xmlHttp.send(null);
    return xmlHttp.responseText;
}

function httpPost(url, body) {
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.open("POST", url);
    xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlHttp.send(JSON.stringify(body));
    return xmlHttp.responseText;
}

function signIn() {
    let password = window.prompt("Admin Password");
    httpGet("/signin/" + password)
    location.reload()
}

function signOut() {
    httpGet("/signout")
    location.reload()
}

function addPinfo(pname, pinfo) {
    let newPInfo = {
        name: pname,
        info: pinfo
    }
    httpPost("/api/pinfos", newPInfo)
}