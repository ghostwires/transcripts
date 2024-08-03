// copied (ha) from top answer for https://stackoverflow.com/questions/2026335/how-to-add-extra-info-to-copied-web-text?rq=1

const copyListener = (event) => {
    const range = window.getSelection().getRangeAt(0),
        rangeContents = range.cloneContents(),
        helper = document.createElement("div");
  
    helper.appendChild(rangeContents);

    var plaintext = helper.innerText;
    plaintext = plaintext.replaceAll('\n\n', '\n');
  
    event.clipboardData.setData("text/plain", `${plaintext}`);
    event.clipboardData.setData("text/html", `${helper.innerHTML}`);
    event.preventDefault();
};
document.addEventListener("copy", copyListener);