function httpGet(url) {
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", url, false);
    xmlHttp.send(null);
    return xmlHttp.responseText;
}

function httpPost(url, body) {
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.open("POST", url, false);
    xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlHttp.send(JSON.stringify(body));
    return xmlHttp.responseText;
}

function httpPut(url, body) {
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.open("PUT", url, false);
    xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlHttp.send(JSON.stringify(body));
    return xmlHttp.responseText;
}

function httpDelete(url) {
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.open("DELETE", url, false);
    xmlHttp.send();
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

function deleteConfig(name) {
    httpDelete("/api/configurations/" + name)
    location.assign("/configurations")
}

function addConfiguration(form) {
    let name = form["configName"].value
    let description = form["configDescription"].value
    let configuration = JSON.parse(httpPost("/api/configurations", {
        "name": name,
        "description": description,
        "showOnAdmin": false
    }))

    let pinfos = JSON.parse(httpGet("/api/pinfos"))

    for (let i = 0; i < pinfos.length; i++) {
        let pinfo = pinfos[i]
        let value = form[pinfo.name].value

        if (value !== "") {
            let pvalue = {
                "pinfo": pinfo["_id"]["$oid"],
                "config": configuration["_id"]["$oid"],
                "value": value
            }

            httpPost("/api/pvalues", pvalue)
        }
    }
}

function editConfiguration(form, configName) {
    let name = form["configName"].value
    let description = form["configDescription"].value
    let updated_config = JSON.parse(httpPut("/api/configurations/" + configName, {
        "name": name,
        "description": description
    }))
    alert(updated_config)

    let pinfos = JSON.parse(httpGet("/api/pinfos"))
    let pvalues = JSON.parse(httpGet("/api/pvalues"))

    for (let i = 0; i < pinfos.length; i++) {
        let pinfo = pinfos[i]
        let value = form[pinfo.name].value

        if (value !== "") {
            alert(value)

            let pvalue = {
                "pinfo": getID(pinfo),
                "config": getID(updated_config),
                "value": value
            }

            alert(pvalue)

            let set_pvalue = pvalues.filter(x => x['pinfo'] === getID(pinfo))
            alert(set_pvalue)
            if (set_pvalue !== undefined) {
                let deleted = httpDelete("/api/pvalues/" + getID(set_pvalue))
                alert(deleted)
            }
            httpPost("/api/pvalues", pvalue)
        }
    }
}

function getID(object) {
    return object["_id"]["$oid"]
}

//TODO: update configuration if name/description changed
//TODO: find pvalues, update
//TODO: create new pvalues for config