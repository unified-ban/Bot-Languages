#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

'''
Traduzione Italiana
__Author__ <https://github.com/clementefnc>
'''

from Params.common import *

# Report level
error = 'error'
warning = 'warning'
info = 'info'

# Testing
test = 'Questo è un messaggio di test!'

# Exception
unhandled = 'Si è verificata una eccezione non gestita.'

# Footers
footer_help = '\n\nScrivi /help per istruzioni.'
footer_delete_delay = '\n\nQuesto messaggio sarà eliminato automaticamente..'

# Log
update_error = "L'aggiornamento %s ha causato un errore: %s."
log_file_header = prefix + 'Log - START\nData: %s\n----------\n\n'

# Support
support_text = '<b>[Supporto]</b>\n%s\n\n<i>- %s</i>'

# Sync
sync = 'Sincronizzazione completata. <b>%s</b> utenti malevoli bloccati.'

# Delete
delete_max = "Possono essere eliminati un massimo di 20 messaggi alla volta."

# Report Channel
reportchannel_start = "Benvenuto nella procedura guidata dove puoi cambiare il canale report per il tuo gruppo.\n\
Prima di tutto crea un nuovo canale (o gruppo) ed aggiungimi come amministratore.\n\
Successivamente inviami un post del canale in questa chat."
reportchannel_setup = "1. Abilita la Dashboard, digita <code>/config</code> nel tuo gruppo \
e clicca su 'Abilita Dashboard' (questa voce è nascosta se già abilitata)\n\
2. Accedi a https://unifiedban.solutions col tuo Telegram account\n\
3. Vai a 'Groups' nel menu e clicca Edit sul tuo gruppo\n\
4. Aggiungi <code>%s</code> nel campo 'User report logs'\n\
5. Clicca save.\n\n\
Ora tutti i tuoi user reports verranno inviati al nuovo canale report."

# Antiscam
scam_block = "L'utente %s è stato limitato per 24h per scam."

# Antiflood (f_)
flood_block = "L'utente {{%s}} è stato limitato per 10 minuti per flood."
flood_unlimited = "Limitazioni rimosse"+footer_delete_delay
f_unlimit = "Rimuovi limitazioni"

# Status
status = "<b>Stato del server</b>\n\
CPU: {cpu}%\n\
Memoria: {memory}%\n\n\
<b>Stato del database</b>\n\
{mysql}"
status_running = "in funzione"
status_stopped = "non in funzione"

# Spamlogic
spamlogic_created = "Nuova logica spam creata con nome %s e sintassi:\n\
<code>%s</code>\n\n\
<b>Metodo:</b> %s\n\
<b>Parametri:</b> %s"

# Configure
configure_prefix = '{{%s}}\n\n'
configure = configure_prefix + '<b>Impostazioni</b>\n\
Configurazione del Bot per questo gruppo.'
configure_update = '\n\n<b>Modifiche salvate.</b> <i>%s</i>'
configure_close = 'Menu impostazioni chiuso.'
configure_lang = configure_prefix + 'Imposta la <b>Lingua</b> del bot per questo gruppo:'
configure_report = configure_prefix + 'Cambia il canale (o gruppo) per le segnalazioni degli utenti dalla Dashboard:'
configure_call = configure_prefix + "Un operatore prenderà a carico la tua richiesta il prima possibile."
configure_sign = configure_prefix + "Dashboard abilitata per il tuo User_ID."
c_instructions = 'Istruzioni'
c_dashboard = 'Dashboard'
c_go_dashboard = 'Vai alla Dashboard'
c_offensive = 'Parole offensive %s'
c_spam = 'Logiche spam %s'
c_flood = 'Antiflood %s'
c_nonwest = 'Caratteri esteri %s'
c_telegram_link = 'Telegram links %s'
c_username = 'Spam nome utente %s'
c_scam = 'Antiscam %s'
c_blacklist = 'Blacklist %s'
c_welcome = 'Benvenuto %s'
c_captcha = 'Captcha %s'
c_user_rtl = 'Blocca RTL in-user %s'
c_language = 'Lingua %s'
c_report_channel = 'Canale report utente'
c_faq = 'FAQ'
c_close = 'Chiudi menu'
c_back = 'Indietro'
c_call_operator = "Chiama un operatore"
c_community_support = "Chiedi supporto"
c_close_group = "Chiudi gruppo"
c_open_group = "Apri gruppo"
c_sign = "Abilita dashboard"
c_news = "Novità/Changelog"

# Reports
report = '<b>[Report]</b>\n%s\n\n\
<b>hash_code:</b> %s'
report_operators = '<b>[Report per gli operatori]</b>\n%s\n\n\
<b>hash_code:</b> %s'
report_get = 'Informazioni richieste:\n\
chat_id: <code>%s</code>\n\
message_id: <code>%s</code>\n\
author_id: <code>%s</code>\n\
author_username: <code>%s</code>\n\
is_bot: <code>%s</code>'
report_startsession = '%s ha iniziato una sessione di supporto.\nchat_id: <code>%s</code>'
report_stopsession = '%s ha fermato una sessione di supporto.\nchat_id: <code>%s</code>'
report_leave = "Bot rimosso dall'operatore: %s\nchat_id: <code>%s</code>"
report_sync = 'Chat <b>%s</b> sincronizzata. <b>%s</b> users blocked.'
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
report_bad = "Messaggio proibito eliminato." + report_common_params
report_spam_deleted = "Messaggio di spam eliminato."
report_spam = report_spam_deleted + report_common_params
report_spam_logic = report_spam_deleted + report_common_params_method + "\n\n\
Questo messaggio di spam è stato rilevato con una spamlogic."
report_nonwest = "Messaggio con caratteri proibiti eliminato." + report_common_params
report_blacklist = "Utente nella Blacklist, rimosso dalla chat" + report_common_params_no_entity
report_scam = "Messaggio di scam eliminato." + report_common_params + "\n\
User limitato per 24h."
report_flood = "Flood bloccato." + report_common_params_no_entity_no_user + "\n\
User limitato per 10m."
report_black = "L'operatore <code>%s</code> ha aggiunto l'Utente <code>%s</code> nella Blacklist dalla chat <code>%s</code>\n\
Motivazione: <code>%s</code>"
report_white = "L'operatore <code>%s</code> ha rimosso l'Utente <code>%s</code> dalla Blacklist."
report_feedback = "Tipologia: %s\n\
Da: %s\n\
Testo:\n<code>%s</code>"
report_feedback_choose = 'Seleziona la tipologia del feedback:'
report_disable = "L operatore %s ha disattivato il bot in chat\n\
<b>Chat:</b> <code>%s</code> \n@%s\n\
<b>Chat_ID:</b> <code>%s</code>\n\
Bot rimosso."
report_call_operator = "%s ha richiesto la presenza di un operatore.\n\
<b>Chat:</b> <code>%s</code> \n@%s"
report_hammer = "Gruppo aperto.\n\
Ecco la lista degli utenti bloccati:\n%s\n\n\
Ogni dato è stato eliminato dai nostri database."
report_hammer_empty = "Gruppo aperto.\n\
Nessun utente bloccato."
report_registration = "Nuovo gruppo registrato.\n\
<b>Chat:</b> <code>%s</code>\n\
<b>Chat_ID:</b> <code>%s</code>"
user_report_header = "<b>[Report Utente]</b>\n\
dalla chat %s\n\n"
user_report = user_report_header + "\
<b>Da:</b> %s\n\
<b>Messaggio:</b>\n<code>%s</code>\n\n\
<b>Link al messaggio:</b> %s"
user_report_sent = "Report Utente inviato correttamente agli amministratori del gruppo."

# Permissions
no_permissions = "L'utente (%s)\n---> non ha (%s) il permesso per: (%s)"

# Errors
no_user_specified = 'Nessun utente specificato.' + footer_help

# Welcome (w)
welcome = 'Ciao {username}, benvenuto su {chat_name}!\nDigita /setrules per il regolamento.'
welcome_set = 'Messaggio di benvenuto aggiornato correttamente.'+footer_delete_delay
welcome_help = 'Scrivi <code>/setwelcome</code> seguito dal nuovo messagio di benvenuto.\n\n\
<b>Variabili disponibili:</b> {username}, {first_name}, {last_name}, {chat_name}.'
welcome_buttons_empty = "Non ci sono pulsanti per questo gruppo.\nDigita /addwelcomebutton per crearne uno."
welcome_buttons_list = "Ecco la lista dei pulsanti per questo gruppo."
welcome_buttons_add = "Nuovo pulsante con nome (%s) creato.."+footer_delete_delay
welcome_buttons_remove = "Pulsante con nome (%s) rimosso."+footer_delete_delay
welcome_buttons_format_error = "Formato errato."+footer_help
welcome_captcha = '\n\n<b>Prova che non sei un robot, clicca il pulsante qui sotto!</b>'
w_captcha = "Non sono un robot!"

# Notes
note_format_error = "Wrong format."+footer_help
note_add = "Nota col nome %s creata con successo."+footer_delete_delay
note_remove = "Nota col nome %s rimossa con successo."+footer_delete_delay

# Rules
rules = '- No spam\n\
- No scam\n\
- Non offendere gli altri utenti\n\
Mantieni un buon comportamento.'
rules_set = 'Regolamento aggiornato correttamente..'+footer_delete_delay
rules_help = 'Scrivi <code>/setrules</code> seguito dal nuovo regolamento.\n\n\
<b>HTML</b> disponibile.'

# Identity
identity = "%s è un operatore certificato di unified/ban.\n\
Come operatore può eseguire manutenzione e supporto."

# Language
language_set = 'Lingua aggiornata correttamente.'+footer_delete_delay
language_help = 'Scrivi <code>/language</code> seguito da una lingua supportata:\n\n\
en_US, it_IT'

# Check
check = 'Ho i seguenti permessi:\n\
<b>Cancellazione messaggi:</b> %s\n\
<b>Ban/Unban utenti:</b> %s\n\n\
<b>Stato:</b>\n%s'
check_true = 'I miei permessi sono configurati correttamente, nessun problema rilevato.'
check_false = 'I miei permessi non sono configurati correttamente. Controlla \
le impostazioni di amministrazione del gruppo o contattami privatamente digitando / start \
per ulteriori informazioni e supporto.'

# Say
say = '<b>Annuncio dagli amministratori del gruppo</b>\n\n%s'
say_no_text = 'Testo non specificato.' + footer_help

# Pin
pin_no_message  = 'Nessun messaggio specificato.' + footer_help

# Ban
ban = '%s è stato bannato.' + footer_delete_delay
unban = 'Ban rimosso per %s.' + footer_delete_delay

# Kick
kick = '%s è stato rimosso dal gruppo.' + footer_delete_delay

# Limit
limit = '%s è stato limitato per 24h.' + footer_delete_delay
unlimit = 'Limite rimosso per %s.' + footer_delete_delay

# Bad
bad = '<code>%s</code> è stata aggiunta alle parole censurate.'+footer_delete_delay
unbad = '<code>%s</code> rimossa dalla lista delle parole censurate.'+footer_delete_delay
badlist = 'La lista delle parole censurate per questo gruppo è disponibile nella <a href="https://unifiedban.solutions">Dashboard</a>.'

# Safe
safe = '<code>%s</code> aggiunto alla lista sicura.'+footer_delete_delay
unsafe = '<code>%s</code> rimosso dalla lista sicura.'+footer_delete_delay
safelist = 'La lista sicura per questo gruppo è disponibile nella <a href="https://unifiedban.solutions">Dashboard</a>.'
wrongsafe = '<code>%s</code> non è un username valido di gruppo o canale.'

# Black
black_header = '{{%s}}\n\
User_ID: %s\n\n'
black_select_motivation = black_header + 'Seleziona una motivazione per inserire %s (%s) in Blacklist:'
black_motivation_other = black_header + 'Scrivi due righe:'
black_done = '<b>%s</b> è stato aggiunto alla Blacklist.\n\
<b>Motivazione:</b>\n\
<code>%s</code>'

# Feedback (f_)
feedback_selection = '{{%s}}\n%s\n' + report_feedback_choose
feedback_no_text = "Testo del feedback non specificato" + footer_help
feedback_sent = "Feedback inviato."
f_suggestion = "Suggerimento"
f_bug = "Segnala Bug"
f_report = "Segnala utente"

# Start
start_text = 'Benvenuto.\n\
Ti aiutero a gestire e proteggere il tuo gruppo.\n\n\
Prima di tutto, aggiungimi come amministratore al tuo gruppo.\n\
Necessito dei seguenti permessi:\n\
- Cancellazione messaggi\n\
- Blocco utenti\n\
nient altro.\n\n\
Fatto?\n\
Controlla la correttezza digitando /check nel tuo gruppo.\n\n\
Tutto è pronto.\n\
Ora puoi modificare le mie impostazioni digitando /config nel tuo gruppo.\n\
Usa la dashboard online per cambiare le mie impostazioni e \
tenere traccia delle mie operazioni.\n\
Prima di tutto, digita /sign nel tuo gruppo per abilitare account.\n\
Poi, visita https://unifiedban.solutions ed accedi con il tuo account di Telegram\n\n\
Hai riscontrato problemi?\n\
Contatta il supporto dalla sezione Supporto della Dashboard.\n\n\
- unified/ban'
start_text_group = 'Contattami in privato.'

# Help
help_text = "<b>unified/ban:</b>\n\
<b>Versione:</b> " + version + "\n\
Questo bot offre una soluzione completa per la gestione e protezione dei gruppi Telegram.\n\n\
/help - Mostra questo messaggio\n\
/report - Invia una segnalazione agli amministratori del gruppo, puoi aggiungere un testo e citare un messaggio\n\
/start - Mostra il messaggio iniziale (privato)\n\
/rules - Mostra il regolamento del gruppo\n\n\
<b>Amministrazione:</b>\n\
/s testo - crea un nuovo annuncio\n\
/pin - metti in evidenza un messaggio (cita un messaggio)\n\
/check - controlla se unified/ban ha i permessi corretti\n\
/kick - rimuovi un utente dal gruppo (cita un messaggio)\n\
/ban - blocca e rimuovi utente dal gruppo (cita un messaggio)\n\
/unban - sblocca nel gruppo (cita un messaggio)\n\
/limit - limita l'invio messaggi dell'utente per 24h \
(cita un messaggio)\n\
/unlimit tempo in minuti - rimuovi limitazioni utente \
(cita un messaggio)\n\
/config - modifica le impostazioni del bot\n\
/bad word - aggiungi una parola censurata nel gruppo (max 30 caratteri)\n\
/unbad word - rimuovi parola censurata nel gruppo\n\
/badlist - mostra le parole censurate nel gruppo\n\
/safe @username - aggiunge un gruppo o canale alla lista sicura\n\
/unsafe @username - rimuove un gruppo o canale dalla lista sicura\n\
/safelist - mostra la lista sicura dei gruppi e canali\n\
/rm - elimina un messaggio (cita un messaggio)\n\
/setwelcome - imposta il messaggio automatico di benvenuto\n\
/addwelcomebutton nome url - crea un nuovo pulsante col nome fornito, nel messaggio di benvenuto\n\
/removewelcomebutton nome - rimuovi il pulsante col nome fornito, dal messaggio di benvenuto\n\
/welcomebuttons - mostra i pulsanti del messaggio di benvenuto\n\
/setrules - importa il testo del regolamento\n\
/language - cambia la lingua del bot in questo gruppo\n\
/setnote hashtag text - aggiungi una nota al gruppo\n\
/removenote hashtag - rimuovi una nota nel gruppo\n\
/feedback - Invia un feedback agli operatori"

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