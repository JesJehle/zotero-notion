# Zotero to Notion integration
The following project tries to implement a sync between a zotero collection and a notion database.
The integration should provide:
* sync of all items in a zotero collection in a notion database
* sync all attributes together with a path to the local pdf file
* sync must be constant, every change in the zotero collection must be reflected in the notion database

# Methods
For fetching the zotero data I want to use the [zotero API](https://www.zotero.org/support/dev/web_api/v3/basics).
For posting the data to notion I use the [notion API](https://developers.notion.com/)
The only problem I see is: How to provide a real time sync?
My best guess is, to implement a listener function via a cron job on some server and run it every second. If the zotero collection changes, the changes get posted to the notion database.

