## Aadhaar Link Check Script

This Python script allows you to check whether your Aadhaar number and PAN Number are linked or not.

![alt text](https://github.com/iamskidrow/aadhar_pan_link_status/blob/main/screenshots/arg_all.png?raw=true)



### Usage

The script provides two methods to input the PAN and Aadhaar numbers:

<strong> Command-line arguments: </strong>
- Use the `-p` or `--pan` option followed by your PAN number.
- Use the `-a` or `--aadhaar` option followed by your Aadhaar number.
 ```
 python aadhaar_link_check.py -p ABCDE1234F -a 123456789012
 ```

<strong> Interactive input: </strong>
- If you don't provide the PAN and Aadhaar numbers as command-line arguments, the script will prompt you to enter them interactively.
```
Enter PAN number: 
Enter Aadhaar number:
```
- Simply follow the prompts in the console and enter your PAN and Aadhaar numbers when requested.

### Results

After providing the required details, the script will send a request to the Income Tax Department's website to check the link status between your PAN and Aadhaar numbers. The script will display the result of the link check on the console.

- If the response shows that your Aadhaar number is linked to your PAN, it means they are connected.
- If the response shows that your Aadhaar number is not linked, it means you need to link them by following the instructions provided by the Income Tax Department.

### Contributing

Contributions to this script are welcome. Feel free to fork the repository, make improvements, and submit pull requests.

### Disclaimer

This script is provided for informational purposes only. Use it responsibly and at your own risk. The script interacts with the Income Tax Department's website, and the results may depend on the availability and accuracy of the website's data. The developer is not responsible for any issues or consequences arising from the use of this script.
