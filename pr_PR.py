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
error = 'erro'
warning = 'atenção'
info = 'informações'

# Testing
test = 'Esta é uma mensagem de teste!'

# Exception
unhandled = 'Ocorreu uma exceção não tratada.'

# Footers
footer_help = '\n\nDigite /help para obter instruções.'
footer_delete_delay = '\n\nEsta mensagem será excluída automaticamente..'

# Log
update_error = 'A atualização %s causou um erro: %s.'
log_file_header = prefix + 'Log - START\nDate: %s\n----------\n\n'

# Support
support_text = '<b>[Apoio, suporte]</b>\n%s\n\n<i>- %s</i>'

# Sync
sync = 'Sincronização concluída. <b>%s</b> usuários maliciosos bloqueados.'

# Delete
delete_max = "No máximo 20 mensagens podem ser excluídas por vez."

# Report Channel
reportchannel_start = "Bem-vindo ao assistente em que você pode alterar o canal de relatório do seu grupo.\n\
Antes de tudo, crie um novo canal (ou grupo) e me adicione como administrador.\n\
Em seguida, envie-me uma postagem no canal neste bate-papo."
reportchannel_setup = "1. Ative seu painel, digite <code> /config </code> no seu grupo \
e clique em 'Ativar painel' (esta voz está oculta se já estiver ativada)\n\
2. Faça login em https://unifiedban.solutions com sua conta Telegram\n\
3. Vá para o menu 'Grupos' e edite seu grupo\n\
4. Adicione <code>%s</code> no campo 'Logs do relatório do usuário'\n\
5. Clique em salvar.\n\n\
Agora todos os seus relatórios de usuários serão enviados para o seu novo canal de relatórios."

# Antiscam
scam_block = "Uer %s limitado por 24h por fraude."

# Antiflood (f_)
flood_block = 'Usuário {{%s}} limitado por 10m para inundação.'
flood_unlimited = "Restrições removidas"+footer_delete_delay
f_unlimit = "Remover restrições"

# Status
status = "<b>Server status</b>\n\
CPU: {cpu}%\n\
Memory: {memory}%\n\n\
<b>Database status</b>\n\
{mysql}"
status_running = "running"
status_stopped = "stopped"

# Spamlogic
spamlogic_created = "Nova lógica de spam criada com o nome% se sintaxe:\n\
<code>%s</code>\n\n\
<b>Method:</b> %s\n\
<b>Params:</b> %s"

# Configure (c_)
configure_prefix = '{{%s}}\n\n'
configure = configure_prefix + '<b>Configurações</b>\n\
Configuração de bot para este grupo.'
configure_update = '\n\n<b>Mudanças salvas.</b> <i>%s</i>'
configure_close = 'Menu de configurações fechado.'
configure_lang = configure_prefix + 'Selecione Bot <b> Idioma </b> para o seu grupo:'
configure_report = configure_prefix + 'Alterar canal (ou grupo) para relatórios de usuários do Painel:'
configure_call = configure_prefix + "Um operador aceitará sua solicitação o mais rápido possível."
configure_sign = configure_prefix + "Painel ativado para seu User_ID."
c_instructions = 'Instruções'
c_dashboard = 'Dashboard'
c_go_dashboard = 'Dashboard'
c_offensive = 'Palavras ofensivas %s'
c_spam = 'Spamlogics %s'
c_flood = 'Antiflood %s'
c_nonwest = 'Non-west chars %s'
c_telegram_link = 'Telegram links %s'
c_username = 'Spam user name %s'
c_scam = 'Antiscam %s'
c_blacklist = 'Blacklist %s'
c_welcome = 'Mensagem de boas-vindas %s'
c_captcha = 'Captcha %s'
c_user_rtl = 'Block RTL in-user %s'
c_language = 'Idioma %s'
c_report_channel = 'Canal de relatório'
c_faq = 'FAQ'
c_close = 'Fechar menu'
c_back = 'De volta'
c_call_operator = "Operador de chamada"
c_community_support = "Peça suporte"
c_close_group = "Close group"
c_open_group = "Grupo aberto"
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
no_user_specified = 'Nenhum usuário especificado.' + footer_help

# Welcome (w)
welcome = 'Olá {username}, bem-vindo ao {chat_name}\Digite /setrules.'
welcome_set = 'Mensagem de boas-vindas atualizada corretamente.'+footer_delete_delay
welcome_help = 'Digite <code> /setwelcome </code> seguido pela nova mensagem de boas-vindas.\n\n\
<b>Variáveis disponíveis:</b> {username}, {first_name}, {last_name}, {chat_name}.'
welcome_buttons_empty = "Não há botões para este grupo.\nDigite /addwelcombutton para criar um."
welcome_buttons_list = "Aqui está a lista de botões para o seu grupo."
welcome_buttons_add = "Novo botão com o nome (%s) criado."+footer_delete_delay
welcome_buttons_remove = "Botão com o nome (%s) removido."+footer_delete_delay
welcome_buttons_format_error = "Formato incorreto."+footer_help
welcome_captcha = '\n\n<b>Teste que você não é um robô, clique no primeiro botão abaixo!</b>'
w_captcha = "Eu não sou um robô!"

# Notes
note_format_error = "Formato incorreto."+footer_help
note_add = "Observe com o nome %s criado com sucesso."+footer_delete_delay
note_remove = "Observe com o nome %s removido com sucesso."+footer_delete_delay

# Rules
rules = '- No spam\n\
- No scam\n\
- Não ofenda outros usuários\n\
Manter um comportamento adequado.'
rules_set = 'Mensagem de regras atualizada corretamente.'+footer_delete_delay
rules_help = 'Digite <code> /setrules </code> seguido pela nova mensagem de regras.\n\n\
<b>HTML</b> acessível.'

# Identity
identity = "%s é um operador unified/ban certificado.\n\
Como operador, ele pode executar manutenção e suporte."

# Language
language_set = 'Idioma atualizado corretamente.'+footer_delete_delay
language_help = 'Digite <code> /language </code> seguido por um código de idioma suportado:\n\n\
en_US, it_IT, pr_PR'

# Check
check = 'Eu tenho as seguintes permissões:\n\
<b>Apagar mensagens:</b> %s\n\
<b>Ban/Unban usuários:</b> %s\n\n\
<b>Status:</b>\n%s'
check_true = 'Minhas permissões estão configuradas corretamente, não há problemas.'
check_false = 'As permissões não estão configuradas corretamente. Verifica a \
configurações de administração do grupo ou entre em contato comigo em particular e digite /start \
para obter mais informações e suporte.'

# Say
say = '<b>Comunicado dos administradores do grupo</b>\n\n%s'
say_no_text = 'Nenhum texto especificado.' + footer_help

# Pin
pin_no_message  = 'Nenhuma mensagem especificada.' + footer_help

# Ban
ban = '%s foi bloqueado.' + footer_delete_delay
unban = 'Bloco removido para %s.' + footer_delete_delay

# Kick
kick = '%s foi chutado.' + footer_delete_delay

# Limit
limit = '%s está limitado por 24h.' + footer_delete_delay
unlimit = 'Limite removido para %s.' + footer_delete_delay

# Bad
bad = '<code>%s</code> adicionado à lista de palavrões.'+footer_delete_delay
unbad = '<code>%s</code> removido da lista de palavrões.'+footer_delete_delay
badlist = 'A lista de palavrões para este grupo está disponível no <a href="https://unifiedban.solutions">Dashboard</a>.'

# Safe
safe = '<code>%s</code> adicionado à lista segura.'+footer_delete_delay
unsafe = '<code>%s</code> removido da lista segura.'+footer_delete_delay
safelist = 'A lista segura para esse grupo está disponível no <a href="https://unifiedban.solutions">Dashboard</a>.'
wrongsafe = '<code>%s</code> não é um nome de usuário de grupo ou canal existente.'

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
feedback_no_text = "Nenhum texto especificado para feedback" + footer_help
feedback_sent = "Feedback enviei."
f_suggestion = "Sugestão"
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
