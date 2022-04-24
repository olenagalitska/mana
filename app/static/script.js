function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

function signIn(){
    var password = window.prompt("Admin Password");
    httpGet("/signin/" + password)
    location.reload()
}

function signOut(){
    httpGet("/signout")
    location.reload()
}