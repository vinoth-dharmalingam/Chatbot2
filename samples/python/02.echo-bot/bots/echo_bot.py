# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount


class EchoBot(ActivityHandler):
    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hi Vinoth! Which State are you from?")

    async def on_message_activity(self, turn_context: TurnContext):
        answer = turn_context.activity.text.strip()
        if answer.lower() == "delaware" or answer.lower() == "de":
            return await turn_context.send_activity("Delaware is a great State!")
        else:
            return await turn_context.send_activity("You should move to Delaware! It's a great State!")
