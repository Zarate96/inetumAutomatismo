from django.core.mail import send_mail, send_mass_mail

def enviomail():
    subject = 'TEMM | {} | {} | {}'.format("remedy", "holding", "sucursal" )
    html_message = """
    <p><a name="_MailAutoSig"><span style="color:black">Estimado Cliente:</span></a></p>

<p>&nbsp;</p>

<p><span style="color:black">Antes que nada le brindamos un cordial saludo agradeciendo su tiempo para comunicarse con nosotros.</span></p>

<p>&nbsp;</p>

<p><span style="color:black">Por este medio&nbsp; le informamos que la incidencia reportada para la sucursal&nbsp; | el servicio&nbsp; </span><strong><u>&ldquo; &rdquo; </u></strong>se est&aacute; atendiendo con&nbsp; el folio <strong> </strong>, al cual se le est&aacute; dando prioridad para que su soluci&oacute;n lo antes posible. Le mantendremos informando el seguimiento y soluci&oacute;n del mismo.</p>

<p>&nbsp;</p>

<p><span style="color:black">Sin m&aacute;s por el momento, quedamos a sus &oacute;rdenes.</span></p>

<p>&nbsp;</p>

<p><span style="color:black">Saludos Cordiales.</span></p>

<p><strong><span style="color:#031a34">Rodrigo Rodr&iacute;guez</span></strong></p>

<p><span style="color:#031a34">Supervisor fijo || GICS</span><br />
<strong><span style="color:#3b3838">Telef&oacute;nica | Movistar M&eacute;xico</span></strong></p>

<p><span style="color:#031a34">M&oacute;vil 5516168305</span></p>

<p>&nbsp;</p>

<p><span style="color:black">Prol. Paseo de la Reforma 1200, Col. Cruz Manca,<br />
Del. Cuajimalpa de Morelos, Ciudad de M&eacute;xico, C.P. 05349</span></p>

<p><a href="mailto:asistenciafijogc.mx@telefonica.com"><span style="color:#0563c1">asistenciafijogc.mx@telefonica.com</span></a><span style="color:black">&nbsp;|</span><a href="http://www.movistar.com.mx/"><span style="color:black">www.movistar.com.mx</span></a><br />
&nbsp;</p>
    """
    message = html_message.format( "remedy","prueba")

    from_email = 'rodrigo-josue.rodriguez@inetum.com'
    recipient_list = ['rodrigo-josue.rodriguez@inetum.com', 'rocoweb001@gmail.com', 'rodrigojrodriguezm@gmail.com' ]

    message1 = (subject, message,from_email , recipient_list )
    message2 = ('Another Subject', 'Here is another message', from_email , recipient_list)

    send_mass_mail((message1, message2), fail_silently=False)