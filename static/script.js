// This simple script adds tweets to the list

function addTweet() {
    // call python file somehow
    //
    // add it to the list
    // so we have to make a get request to my little local flask server
    var xhr = new XMLHttpRequest();
    xhr.open('GET','/getTweet', true);
    xhr.send();
    xhr.onload = function () {
        console.log("Loaded request... adding to list");
        var tweet = xhr.response;
        var list = document.getElementById('tweetList');
        var entry = document.createElement('li');
        entry.appendChild(document.createTextNode(tweet));
        list.appendChild(entry);
    }
}

