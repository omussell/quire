# quire

Generate a One Time Pad notebook for unbreakable encryption. [What is a One Time Pad?](https://en.wikipedia.org/wiki/One-time_pad)

have a way to convert plaintext into numbers
Include hash of the generated OTP book/page so we can validate it hasnt been tampered.
- Output a working one-time pad in a format suitable for printing and copying.
- Output the language to plaincode conversion table.
- Output the codebook, if used.
- Allow the ability to use conversion tables for different languages
- Allow the ability for the user to provide their own conversion table

For page identifier, feed random bytes into blake3

When run without arguments, print the help page.

When run with XYZ flag, generates a one time pad, including codebook and conversion table and prints to stdout

If XYZ flag is given, write to file instead of stdout

The one time pad is arranged as follows:

- 53 pages
- The 1st page of the book displays the serial number of the whole pad itself, in the form of a base64 hash of each of the page hashes. This also constitutes as an identifier for the pad.
- The 52nd page of the book is the codebook of common words and phrases
- The 53rd page of the book is the conversion table
- The intervening pages display one time pads
- For each OTP page, groups of five numbers separated by a single space, arranged in five columns and ten rows
- Pages are separated by 30 hyphen characters.

What are the chances that the KEYID, the first group in the OTP, is a duplicate between pads? If the same KEYID appears more than once then you wont be able to use it as an identifier?

Should include the conversion tables for the other languages
Should include blank copies of the codebooks so you can make your own

## Summary

A good paper explaining how one-time pads work is [here](http://users.telenet.be/d.rijmenants/papers/one_time_pad.pdf)

## How a One-Time Pad Works

### Message Preparation

The message needs to be converted into plaincode first, which means using the conversion table which has been optimised for English so that frequently used letters are single-digit values.

- Spaces are represented by 99 (SPC)
- A comma and apostrophe are both represented by 93 (')
- Parentheses are opened and closed with 94 ( )
- Numbers are written out three times to exclude errors and they are preceded and followed by 90 (NUM)
- Punctuation is allowed within number values (like 3.5)
- The request code 98 (REQ) can be replaced by a question mark

```
M  E  E  T  I  N  G       A  T       1    4       P   M       I  N      N  Y   (.)
79 2  2  6  3  4  74  99  1  6  90  111  444  90  80  79  99  3  4  99  4  88  91

S  I  Z  E  =      3  .   5      F  E  E  T
83 3  89 2  97 90 333 91 555 90  73 2  2  6
```

The codebook prefix CODE (0) precedes three-digit codebook values. Spaces are unnecessary before and after codebook codes.

```
REQUEST  N  E  W   PASSPORT  F  O R  FLIGHT  (.)  UNABLE TO  U  S  E  FERRY
98       4  2  86  0587      73 5 82 0352    91   0884       84 83 2  0343
```

### Encryption

#### Pad Identifier

The receiver needs to know which one-time pad is used. The first group of the one-time pad is used as the key indicator.

This group should never be used in the encryption process. Dont send a serial number like a page number (00001) along with the message because this would reveal the number of messages that were sent and their order.

#### How to encrypt

- Write the plaincode digits of the converted text in groups of five digits
- Skip the first group of the one-time pad
- Write the digits of the one-time pad beneath them
- Complete the last group (padding) with full stops (9191...)
- Subtract the one-time pad digits from the plaincode digits, one by one, from left to right and by modulo 10 (e.g. 5 - 9 = 6 because [1]5 - 9 = 6)

Example:

```
M  E  E  T  I  N  G       A  T       1    4       P   M       I  N      N  Y   (.)
79 2  2  6  3  4  74  99  1  6  90  111  444  90  80  79  99  3  4  99  4  88  91

Plaincode   : KEYID  79226  34749  91690  11144  49080  79993  49948  89191
OTP Key (-) : 68496  47757  10126  36660  25066  07418  79781  48209  28600
              -------------------------------------------------------------
Ciphertext  : 68496  32579  24623  65030  96188  42672  00212  01749  61591
```

### Message Transmission

- Arrange the ciphertext into five groups per row
- If the message is to be sent by radio/voice/morse/telephone, relay each group twice to avoid errors
- If the receiver has a call sign, repeat it three times at the beginning of the message

```
# Call sign is 401

401 401 401

68496  32579  24623  65030  96188
42672  00212  01749  61591
```

### Decryption

#### Pad Identifier

Check the first group against the first group of your one-time pad. This group isnt used for encryption, only pad identification.

#### How to decrypt

- Write the ciphertext digits in groups of five digits
- Skip the first group of the one-time pad
- Write the digits of the one-time pad beneath them
- Add the one-time pad digits to the ciphertext digits, one by one, from left to right and by modulo 10 (e.g. 9 + 6 = 5)

```
Ciphertext  : 68496  32579  24623  65030  96188  42672  00212  01749  61591
OTP Key (-) : 68496  47757  10126  36660  25066  07418  79781  48209  28600
              -------------------------------------------------------------
Plaincode   : KEYID  79226  34749  91690  11144  49080  79993  49948  89191
```

#### Message conversion

- Use the conversion table to convert the digits into their respective characters
- If the next digit is between 1 and 6, it represents a single-sigit value
- If the next digit is 7, 8, or 9, it represents a double-digit value and we have to append the following digit
- If the next digit is 0, it will be followed by a three-digit code that represents a value from the codebook
- If the next double-digit value is 90, then any following three-digit values will represent numbers

```
79 2  2  6  3  4  74  99  1  6  90  111  444  90  80  79  99  3  4  99  4  88  91
M  E  E  T  I  N  G       A  T       1    4       P   M       I  N      N  Y   (.)
```
