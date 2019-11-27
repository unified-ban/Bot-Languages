#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

'''
English translation
__Author__ <send@mirko.pm> Mirko Brombin
'''

from Params.common import *

# Report level
error = 'error'
warning = 'warning'
info = 'info'

# Testing
test = 'This is a test message!'

# Exception
unhandled = 'Unhandled Exception occurred.'

# Footers
footer_help = '\n\nType /help for instructions.'
footer_delete_delay = '\n\nThis message will be automatically deleted..'

# Log
update_error = 'Update %s caused an error: %s.'
log_file_header = prefix + 'Log - START\nDate: %s\n----------\n\n'

# Support
support_text = '<b>[Support]</b>\n%s\n\n<i>- %s</i>'

# Sync
sync = 'Synchronization finished. <b>%s</b> malicious users blocked.'

# Delete
delete_max = "A maximum of 20 messages can be deleted at a time."

# Report Channel
reportchannel_start = "Welcome to the wizard where you can change the report channel for your group.\n\
First of all create a new channel (or group) and add me as an administrator.\n\
Then send me a channel post in this chat."
reportchannel_setup = "1. Enable your Dashoard, type <code>/config</code> in your group \
and click on 'Enable Dashboard' (this voice is hidden if already enabled)\n\
2. Login to https://unifiedban.solutions with yout Telegram account\n\
3. Go to 'Groups' menu and edit your group\n\
4. Add <code>%s</code> on 'User report logs' field\n\
5. Click save.\n\n\
Now all your user reports will be sent to your new report channel."

# Antiscam
scam_block = "User %s limited for 24h for scam."

# Antiflood (f_)
flood_block = 'User {{%s}} limited for 10m for flood.'
flood_unlimited = "Restrictions removed"+footer_delete_delay
f_unlimit = "Remove restrictions"

# Status
status = "<b>Server status</b>\n\
CPU: {cpu}%\n\
Memory: {memory}%\n\n\
<b>Database status</b>\n\
{mysql}"
status_running = "running"
status_stopped = "stopped"

# Spamlogic
spamlogic_created = "New spam logic created with name %s and syntax:\n\
<code>%s</code>\n\n\
<b>Method:</b> %s\n\
<b>Params:</b> %s"

# Configure (c_)
configure_prefix = '{{%s}}\n\n'
configure = configure_prefix + '<b>Settings</b>\n\
Bot configuration for this group.'
configure_update = '\n\n<b>Changes saved.</b> <i>%s</i>'
configure_close = 'Settings menu closed.'
configure_lang = configure_prefix + 'Select Bot <b>Language</b> for your group:'
configure_report = configure_prefix + 'Change channel (or group) for user reports from Dashboard:'
configure_call = configure_prefix + "An operator will accept your request as soon as possible."
configure_sign = configure_prefix + "Dashboard enabled for your User_ID."
c_instructions = 'Instructions'
c_dashboard = 'Dashboard'
c_go_dashboard = 'Go to Dashboard'
c_offensive = 'Offensive words %s'
c_spam = 'Spamlogics %s'
c_flood = 'Antiflood %s'
c_nonwest = 'Non-west chars %s'
c_telegram_link = 'Telegram links %s'
c_username = 'Spam user name %s'
c_scam = 'Antiscam %s'
c_blacklist = 'Blacklist %s'
c_welcome = 'Welcome message %s'
c_captcha = 'Captcha %s'
c_user_rtl = 'Block RTL in-user %s'
c_language = 'Language %s'
c_report_channel = 'User report channel'
c_faq = 'FAQ'
c_close = 'Close menu'
c_back = 'Back'
c_call_operator = "Call operator"
c_community_support = "Ask for support"
c_close_group = "Close group"
c_open_group = "Open group"
c_sign = "Enable dashboard"
c_news = "News/Changelog"

# Reports
report = '<b>[Report]</b>\n%s\n\n\
<b>hash_code:</b> %s'
report_operators = '<b>[Report for operators]</b>\n%s\n\n\
<b>hash_code:</b> %s'
report_get = 'Requested informations:\n\
chat_id: <code>%s</code>\n\
message_id: <code>%s</code>\n\
author_id: <code>%s</code>\n\
author_username: <code>%s</code>\n\
is_bot: <code>%s</code>'
report_startsession = '%s started a support session.\nchat_id: <code>%s</code>'
report_stopsession = '%s stopped the support session.\nchat_id: <code>%s</code>'
report_leave = 'Bot removed by operator: %s\nchat_id: <code>%s</code>'
report_sync = 'Chat <b>%s</b> synchronized. <b>%s</b> users blocked.'
report_common_params = "\n\n\
<b>Chat:</b> <code>%s</code>\n\
<b>Type:</b> <code>%s</code>\n\
<b>Entity:</b> <code>%s</code>\n\
<b>Author:</b> <code>%s</code>\n\
<b>User_ID:</b> <code>%s</code>\n"
report_common_params_method = "\n\n\
<b>Chat:</b> <code>%s</code>\n\
<b>Type:</b> <code>%s</code>\n\
<b>Spamlogic:</b> <code>%s</code>\n\
<b>Author:</b> <code>%s</code>\n\
<b>User_ID:</b> <code>%s</code>\n"
report_common_params_no_entity = "\n\n\
<b>Chat:</b> <code>%s</code>\n\
<b>Type:</b> <code>%s</code>\n\
<b>Author:</b> <code>%s</code>\n\
<b>User_ID:</b> <code>%s</code>\n"
report_common_params_no_entity_no_user = "\n\n\
<b>Chat:</b> <code>%s</code>\n\
<b>Type:</b> <code>%s</code>\n\
<b>User_ID:</b> <code>%s</code>\n"
report_bad = "Prohibited message deleted." + report_common_params
report_spam_deleted = "Spam message deleted."
report_spam = report_spam_deleted + report_common_params
report_spam_logic = report_spam_deleted + report_common_params_method + "\n\n This spam message was detected with a spamlogic."
report_nonwest = "Non West message deleted." + report_common_params
report_blacklist = "User in Blacklist, removed from chat" + report_common_params_no_entity
report_scam = "Scam message deleted." + report_common_params + "\n\
User limited for 24h."
report_flood = "Flood blocked." + report_common_params_no_entity_no_user + "\n\
User limited for 10m."
report_black = "Operator <code>%s</code> added User <code>%s</code> to the Blacklist from chat <code>%s</code>\n\
Motivation: <code>%s</code>"
report_white = "Operator <code>%s</code> removed User <code>%s</code> from the Blacklist."
report_feedback = "Type: %s\n\
From: %s\n\
Text:\n<code>%s</code>"
report_feedback_choose = 'Select feedback type:'
report_disable = "Operator %s disabled bot in chat\n\
<b>Chat:</b> <code>%s</code> \n@%s\n\
<b>Chat_ID:</b> <code>%s</code>\n\
Bot removed."
report_call_operator = "%s requested an operator.\n\
<b>Chat:</b> <code>%s</code> \n@%s"
report_hammer = "Group is open.\n\
Here is the list of blocked users:\n%s\n\n\
Each data has been deleted from our databases."
report_hammer_empty = "Group is open.\n\
No blocked users."
report_registration = "New registered group.\n\
<b>Chat:</b> <code>%s</code>\n\
<b>Chat_ID:</b> <code>%s</code>"
user_report_header = "<b>[User Report]</b>\n\
from chat %s\n\n"
user_report = user_report_header + "\
<b>From:</b> %s\n\
<b>Message:</b>\n<code>%s</code>\n\n\
<b>Link to message:</b> %s"
user_report_sent = "User report sent correctly to group administrators."

# Permissions
no_permissions = 'User (%s)\n---> have not (%s) permissions for scope: (%s)'

# Errors
no_user_specified = 'No user specified.' + footer_help

# Welcome (w)
welcome = 'Hi {username}, welcome to {chat_name}\nType /setrules.'
welcome_set = 'Welcome message updated correctly.'+footer_delete_delay
welcome_help = 'Type <code>/setwelcome</code> followed by the new welcome message.\n\n\
<b>Available variables:</b> {username}, {first_name}, {last_name}, {chat_name}.'
welcome_buttons_empty = "No buttons for this group.\nType /addwelcomebutton to create one."
welcome_buttons_list = "Here is the list of buttons for your group."
welcome_buttons_add = "New button with name (%s) created."+footer_delete_delay
welcome_buttons_remove = "Button with name (%s) removed."+footer_delete_delay
welcome_buttons_format_error = "Wrong format."+footer_help
welcome_captcha = '\n\n<b>Test that you are not a robot, click the first button below!</b>'
w_captcha = "I'm not a robot!"

# Notes
note_format_error = "Wrong format."+footer_help
note_add = "Note with the name %s successfully created."+footer_delete_delay
note_remove = "Note with the name %s successfully removed."+footer_delete_delay

# Rules
rules = '- No spam\n\
- No scam\n\
- Do not offend other users\n\
Maintain proper behavior.'
rules_set = 'Rules message updated correctly.'+footer_delete_delay
rules_help = 'Type <code>/setrules</code> followed by the new rules message.\n\n\
<b>HTML</b> available.'

# Identity
identity = "%s is a certified unified/ban operator.\n\
As an operator he can perform maintenance and support."

# Language
language_set = 'Language updated correctly.'+footer_delete_delay
language_help = 'Type <code>/language</code> followed by a supported locale:\n\n\
en_US, it_IT'

# Check
check = 'I have following permissions:\n\
<b>Delete messages:</b> %s\n\
<b>Ban/Unban users:</b> %s\n\n\
<b>Status:</b>\n%s'
check_true = 'My permissions are configured correctly, there are no problems.'
check_false = 'The permissions are not configured correctly. Check the \
group administration settings or contact me privately and type / start \
for more information and support.'

# Say
say = '<b>Announcement by group administrators</b>\n\n%s'
say_no_text = 'No text specified.' + footer_help

# Pin
pin_no_message  = 'No message specified.' + footer_help

# Ban
ban = '%s has been banned.' + footer_delete_delay
unban = 'Ban removed for %s.' + footer_delete_delay

# Kick
kick = '%s has been kicked.' + footer_delete_delay

# Limit
limit = '%s has been limited for 24h.' + footer_delete_delay
unlimit = 'Limit removed for %s.' + footer_delete_delay

# Bad
bad = '<code>%s</code> added to bad words list.'+footer_delete_delay
unbad = '<code>%s</code> removed from bad words list.'+footer_delete_delay
badlist = 'The list of bad words for this group is available from the <a href="https://unifiedban.solutions">Dashboard</a>.'

# Safe
safe = '<code>%s</code> added to safe list.'+footer_delete_delay
unsafe = '<code>%s</code> removed from safe list.'+footer_delete_delay
safelist = 'The safe list for this group is available from the <a href="https://unifiedban.solutions">Dashboard</a>.'
wrongsafe = '<code>%s</code> is not an existing group or channel username.'

# Black
black_header = '{{%s}}\n\
User_ID: %s\n\n'
black_select_motivation = black_header + 'Select a motivation to add %s (%s) in Blacklist:'
black_motivation_other = black_header + 'Write a few lines:'
black_done = '<b>%s</b> has been added to the Blacklist.\n\
<b>Motivation:</b>\n\
<code>%s</code>'

# Feedback
feedback_selection = '{{%s}}\n%s\n' + report_feedback_choose
feedback_no_text = "No text specified for feedback" + footer_help
feedback_sent = "Feedback sent."
f_suggestion = "Suggestion"
f_bug = "Report Bug"
f_report = "Report user"

# Start
start_text = 'Welcome.\n\
I will help you manage and protect your ou\n\n\
First, add me to your group administrators list.\n\
I need the following permissions:\n\
- Delete messages\n\
- Block users\n\
nothing else.\n\n\
Done?\n\
Check the correct operation by typing /check in your group.\n\n\
Everything is ready.\n\
Now you can change my settings by typing /config in your group.\n\
There is an online dashboard from which you can change my settings and \
keep track of my operation.\n\
First, type /sign in your group to enable your account.\n\
Next, visit https://unifiedban.solutions and log in through your Telegram \
account.\n\n\
Any problems?\n\
Contact support from the Dashboard Support section.\n\n\
- unified/ban'
start_text_group = 'Contact me in private.'

# Help
help_text = '<b>unified/ban:</b>\n\
<b>Version:</b> ' + version + '\n\
<b>FAQ:</b> https://unifiedban.solutions/faq\n\
This bot offers a complete solution for managing and protecting Telegram \
groups.\n\n\
/help - Show this message\n\
/report - Send a report to the group administrators, can add a text and quote a message\n\
/start - Show the start message (private)\n\
/rules - Show rules\n\n\
<b>Admin:</b>\n\
/s text - create new announcement\n\
/pin - pin a message (use as reply)\n\
/check - check if unified/ban has the right group permissions\n\
/kick - remove user from group (use as reply)\n\
/ban - block and remove user from group (use as reply)\n\
/unban - unblock from group (use as reply)\n\
/limit - limit user send message for 24h \
(use as reply)\n\
/unlimit time in minutes - remove user restrictions \
(use as reply)\n\
/config - edit the bot settings\n\
/bad word - add bad word for the group (max 30 chars)\n\
/unbad word - remove bad word for group\n\
/badlist - show bad words for group\n\
/safe @username - add group or channel to safelist\n\
/unsafe @username - remove group or channel from safelist\n\
/safelist - show the safe list of groups and channels\n\
/rm - delete a message (use as reply)\n\
/setwelcome - set automatic welcome message text\n\
/addwelcomebutton name url - create new button in welcome message with name and url\n\
/removewelcomebutton name - remove button with name in welcome message\n\
/welcomebuttons - show welcome message buttons\n\
/setrules - set rules text for group\n\
/language - change bot language for group\n\
/setnote hashtag text - create new note for group\n\
/removenote hashtag - remove note grom group\n\
/feedback - Send feedback to operators'

# Daemon
class daemon:
	running = 'Instance is running as pid %s.'
	not_running = 'Instance is not running.'
	unknow = 'Unknow command.'
	start = 'Starting..'
	stop = 'Stopping..'
	debug = 'Debugging..'
	restart = 'Restarting..'
	usage = 'Usage: %s start|stop|restart|status'

# Daemon shell
class daemon_shell:
	running = prefix_ok + daemon.running
	not_running = prefix_fail + daemon.not_running
	unknow = prefix_fail + daemon.unknow
	start = prefix_ok + daemon.start
	stop = prefix_ok + daemon.stop
	debug = prefix_ok + daemon.debug
	restart = prefix_ok + daemon.restart
	usage = prefix_bold + daemon.usage