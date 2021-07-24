from pyzotero import zotero
from secrets import ZOTERO_API_KEY, ZOTERO_USER_ID, ZOTERO_GROUP_ID


library_type = "group"

zot = zotero.Zotero(ZOTERO_GROUP_ID, library_type, ZOTERO_API_KEY)
top = zot.top(limit=2)
# TODO #1 It seems the location of the actual pdf is not provided
print(top)
