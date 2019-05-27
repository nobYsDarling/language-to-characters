# language-to-characters
Mapping iso-language names their iso codes (639-1 and 639-2), to used characters in this language:

```
[{
    characters: ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz, 
    language_name: English, 
    iso_639_1: en, 
    iso_639_2: eng
}, ...]
```

I might need this for my master thesis. It's bootstrapped, converted by some scripts. It's based on mainly two Wikipedia articles:
 - [Language recognition chart](https://en.wikipedia.org/wiki/Wikipedia:Language_recognition_chart)

Only took languages of the latin, cyrillic, brahamic, and arabic alphabet here and interpreted the lists as cascading. I removed some languages, I don't need or I think there is too less information to work with.

 - [List of ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)

Finally I mapped language names with their iso codes.

May be this helps. I did most of the processing by scripting. But there is no guarantee what so ever, that this is valid.

Feel free to contribute <3