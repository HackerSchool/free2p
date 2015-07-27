var URL = 'http://192.168.0.111:8080/occupation';


function main() {
    chrome.storage.onChanged.addListener(function(changes) {
        if ('url' in changes) {
            URL = changes.url.newValue;
        }
    });

    chrome.storage.sync.get('url', function(items) {
        if (items.url && items.url != '') {
          URL = items.url;
        } else {
          chrome.storage.sync.set({ url: URL });
        }

        chrome.alarms.onAlarm.addListener(updateState);
        chrome.alarms.create({ delayInMinutes: 0, periodInMinutes: 0.1 });
    });
}


function updateState() {
    if (URL && URL != '') {
        $.get(URL).then(function(data) {
            //data = Math.random() > 0.5 ? 'free' : 'busy';
            //console.log(data)

            switch (data) {
              case 'free':
                icon = 'free.png';
                msg = 'do what you gotta do';
                break;
              case 'busy':
                icon = 'busy.png';
                msg = 'hold your horses mate';
                break;
              default:
                icon = 'unknown.png';
                msg = '';
            }

            chrome.browserAction.setIcon({ path: icon });
            chrome.browserAction.setTitle({ title: msg });
        });
    }
}


main();
