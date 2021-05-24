**Make sure your CSV contains all the features in the below list**

|**Sl. No.**               |Feature Name                          |Description                         |
|----------------|-------------------------------|-----------------------------|
|01|duration           |    Total duration of the network connection        |
|02       |protocol_type            |Types of Protocol used for making the connection (such as TCP ,UDP....)             |
|03          |service| Network service on the destination, e.g., http, telnet, etc.|
|04          |flag|Normal or error status of the connection|
|05          |src_bytes|Number of data bytes sent from source to destination|
|06          |dst_bytes| Number of data bytes received at single connection from sender node|
|07          |land|1 if connection is from/to the same host/port; 0 otherwise|
|08          |hot| Number of hot indicators displayed in the packet|
|09          |logged_in|1 if successfully logged in; 0 otherwise|
|10          |num_comprimised| Number of compromised conditions|
|11          |su_attempted| 1 if Su-root command attempted; 0 otherwise|
|12          |num_root| Number of root accesses and operations considered during connection|
|13          |num_file_creations| Number of file creation operations during the connection|
|14          |is_host_login|1 if the login belongs to the host list; 0 otherwise|
|15          |is_guest_login|1 if the login is a guest login; 0 otherwise|
|16          |count| Number of connections to the same host as the current connection in the past two seconds|
|17          |srv_count| Number of connections requested for same service i.e., port number|
|18          |serror_rate|Percentage of connections that that activates the flag among the connections grouped in count |
|19          |srv_serror_rate|Percentage of connections that have SYN errors|
|20          |reerror_rate|Percentage of connections that have REJ errors|
|21          |srv_rerror_rate|Percentage of connections that activates the flag (REJ) among the connections grouped in count|
|22          |same_srv_rate|Percentage of connections to the same service grouped in the count|
|23          |srv_diff_host_rate|The sum of connections (in percentage) that requested different receiver node connections grouped in count (srv_count = 24)|
|24          |dst_host_count|Sum of connections have same receiver IP address|
|25          |dst_host_srv_count|Sum of connections (in percentage) consists of same port number Sum of connections (in percentage) consists of same port number|
|26          |dst_host_same_srv_rate|Sum of connections (in percentage) requested different service connections grouped in count (Dst_Host_Count = 32)|
|27          |dst_host_same_srv_port_rate|Sum of connections (in percentage) requested same sender port connections grouped in count (Dst_Host_Srv_Count = 33)|
|28          |dst_host_serror_rate|Sum of connections (in percentage) initiated for flag (S0, S1, S2, and S3) grouped in count (Dst_Host_Count = 32)|
|29          |dst_host_srv_serror_rate|Sum of connections (in percentage) initiated for flag (S0, S1, S2, and S3) grouped in count|
|30          |dst_host_rerror_rate|Sum of connections (in percentage) initiated for flag (REJ) grouped in count|
|31          |dst_host_srv_rerror_rate|Sum of connections (in percentage) initiated for flag (REJ) grouped in count (Dst_Host_Srv_Count = 33)|
