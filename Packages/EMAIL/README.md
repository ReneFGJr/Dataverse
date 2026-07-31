Ajuste o nome

   <mail-resource auth="false" host="smtp.gmail.com" from="app.email.dvn@gmail.com" user="app.email.dvn@gmail.com" jndi-name="mail/notifyMailSession">
     <property name="mail.smtp.port" value="465"></property>
     <property name="mail.smtp.socketFactory.fallback" value="false"></property>
     <property name="mail.smtp.socketFactory.port" value="465"></property>
     <property name="mail.smtp.socketFactory.class" value="javax.net.ssl.SSLSocketFactory"></property>
     <property name="mail.smtp.auth" value="true"></property>
     <property name="mail.smtp.password" value="asdkgqogvyecineuzxdtge"></property>
   </mail-resource>


   ./asadmin create-javamail-resource --mailhost [smtp.office365.com] --mailuser [datarepository\@ipen\.br] --fromaddress [br] --property mail.smtp.auth=[true]:mail.smtp.password=[SENHA]:mail.smtp.port=[587]:mail.smtp.socketFactory.port=[587]:mail.smtp.socketFactory.fallback=[false]:mail.smtp.socketFactory.class=[javax.net.ssl.SSLSocketFactory] mail/notifyMailSession