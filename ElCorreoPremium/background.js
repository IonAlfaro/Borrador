
chrome.tabs.onUpdated.addListener( function (tabId, changeInfo, tab) {
	if(changeInfo.status == 'loading'){
		pararPagina();	
	}
	if (changeInfo.status == 'complete') {
  		//var element = document.getElementsByClassName("aviso-pagina");
		borrarCookie();
	}
});

function borrarCookie(){
chrome.cookies.getAll({domain: "elcorreo.com"}, function(cookies) {
    for(var i=0; i<cookies.length;i++) {
    	console.log("LA COOKIE: "+cookies[i]);
        chrome.cookies.remove({url: "http://elcorreo.com" + cookies[i].path, name: cookies[i].name});
    }
});
}

function pararPagina(){
  chrome.tabs.getSelected(null, function(tab) {
    var jsRunner = {'code': 'window.stop()'};
    chrome.tabs.executeScript(tab.id, jsRunner);
  });
}