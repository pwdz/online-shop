const profileContainer = document.getElementById("profileMainContainer");
const profileTab = document.getElementById("profileTab");
const profileContainerInnerHtml = document.body.innerHTML;

function clickProfileTab() {
    profileTab.style.color = "rgb(54, 54, 54)";
    profileTab.style.backgroundColor = "rgb(238, 238, 238)";
    document.body.innerHTML = profileContainerInnerHtml;
    console.log("unja");
}

function clickProfileReciptTab() {
    profileTab.style.color = "rgb(238, 238, 238)";
    profileTab.style.backgroundColor = "rgb(247, 247, 247)";
    const iframe = document.getElementById("profileReceiptHtml");
    if (iframe.parentNode) {
        var savedNode = iframe.parentNode.removeChild(iframe);
    }

    while (document.body.firstChild) {
        document.body.removeChild(document.body.firstChild);
    }
    console.log(savedNode.contentWindow);
    console.log(savedNode.contentDocument);
    var y = (savedNode.contentWindow || savedNode.contentDocument);
    if (y.document) y = y.document;
    console.log(y);
    document.body.appendChild(savedNode);
    savedNode.style.display = "block"
    savedNode.style.width = "100%"
    savedNode.style.height = "100%"

}

