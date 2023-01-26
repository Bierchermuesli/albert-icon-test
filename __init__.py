# -*- coding: utf-8 -*-

"""This is a simple python for Icon test, no difference of the source (xdg,svg)"""

from albert import *

md_iid = "0.5"
md_version = "1.0"
md_name = "ICO Test"
md_description = "Test the icons python API 0.5"
md_license = "MIT"
md_url = "https://example.com"
md_maintainers = "@bierchermüesli"


class Plugin(QueryHandler):
    def id(self):
        return "ico";

    def name(self):
        return "somename";

    def description(self):
        return "somedesc";

    def initialize(self):
        info("initialize")

    def finalize(self):
        info("finalize")

    def extensions(self):
        return [self.e]

    def handleQuery(self, query):

        at_the_end = []

        item = Item()
        item.id ="foo"
        item.icon = ['xdg:albert']
        item.text = '1.1 Albert'
        item.subtext = "via Item Object and at_the_end.append ID:foo"
        at_the_end.append(item)

        debug("item1.1 Ico:"+ str(item.icon))
        debug("item1.1 ID:"+ item.id)
        del(item)

        item = Item()
        item.icon = ['xdg:ac-adapter']
        item.text = '1.2. AC'
        item.subtext = "via Item Object and at_the_end.append - ID:unset"
        at_the_end.append(item)

        debug("item1.2 Ico:"+ str(item.icon))
        debug("item1.2 ID:"+ item.id)

        itemcomputer = Item()
        itemcomputer.icon = ['xdg:computer']
        itemcomputer.text = '2. Computer'
        itemcomputer.subtext = 'seperate Item Object and query.add ID:unset'
        query.add(itemcomputer)

        debug("itemcomputer Ico:"+ str(itemcomputer.icon))
        debug("itemcomputer ID:"+ itemcomputer.id)


        query.add(Item(
            text = "3. Phone",
            id = "phone",
            subtext = "direct query.add - ID:phone",
            icon=['xdg:phone'],
        ))

        query.add(Item(
            text = "4. Mouse",
            subtext = "direct query.add. ID:unset",
            icon=['xdg:mouse'],
        ))

        query.add(at_the_end)
