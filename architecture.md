When run without arguments, print the help page.

When run with XYZ flag, generates a one time pad, including codebook and conversion table and prints to stdout

If XYZ flag is given, write to file instead of stdout

The one time pad is arranged as follows:

- 53 pages
- The 1st page of the book displays the serial number of the whole pad itself, in the form of a base64 hash of each of the page hashes. This also consistutes as an identifier for the pad.
- The 52nd page of the book is the codebook of common words and phrases
- The 53rd page of the book is the conversion table
- The intervening pages display one time pads
- For each OTP page, groups of five numbers separated by a single space, arranged in five columns and ten rows
- Pages are separated by 30 hyphen characters.





What are the chances that the KEYID, the first group in the OTP, is a duplicate between pads? If the same KEYID appears more than once then you wont be able to use it as an identifier?

Can we use a Trusted Execution Environment like Intel SGX or ARM TrustZone? If we can, make it so that it detects which CPU type is being used and decide how to run.

Should include the conversion tables for the other languages
Should include blank copies of the codebooks so you can make your own
