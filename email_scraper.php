<?php
$hostname = '{imap.gmail.com:993/imap/ssl}INBOX';
$username = 'ENTER_EMAIL_ACCOUNT_HERE@gmail.com';
$password = 'ENTER_PASSWORD_HERE';

while(1){
	/* Try to connect */
	$inbox = imap_open($hostname,$username,$password) or die('Cannot connect to Gmail: ' . imap_last_error());

	/* Grab emails */
	$emails = imap_search($inbox,'UNSEEN FROM "5194011120@txt.bell.ca"');

	if($emails) {
	
		/* Begin output var */
		$output = '';
	
		/* Put the newest emails on top */
		rsort($emails);
	
		foreach($emails as $email_number) {
		
			/* Get information specific to this email */
			$overview = imap_fetch_overview($inbox,$email_number,0);
			$message = imap_fetchbody($inbox,$email_number,2);
			/* Output the email body */
			$output.= $overview[0]->from.';';
			$output.= $message;
		}
		$myfile = fopen("garage_output.txt", "w") or die("Unable to open file!");
		echo $output;
		echo PHP_EOL;
		fwrite($myfile, $output);
		fclose($myfile);	
		break;
	}
    /* Don't need to consistently poll - once every 7 seconds is adequate */
	sleep(7); 

	/* Close the connection */
	imap_close($inbox);
}
?>
