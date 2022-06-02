LinkedIn Reply Builder

> Politely decline, fast!

## Usage

It will prompt for names:

```
Input name (or empty string to exit)

> Another name:John
> Prefix?: The job sounds great
Copy generated for John

> Another name:Jane
> Prefix?: 
Copy generated for Jane
```


```
Input name (or empty string to exit)

Another name:John

Prefix?:The job sounds great
Copy generated for John

Another name:Jane

Prefix?:
Copy generated for Jane

Another name: 
```

and your pasteboard looks like:

```
Hi John,

Thanks for reaching out with the offer.
The job sounds great, but I'm very happy in my role at ACME Org. and am not looking for a move.

Hope you find someone suitable.

Thanks,
Jamie


Hi Jane,

Thanks for reaching out with the offer.
Right now I'm very happy in my role at ACME. Org  and am not looking for a move.

Hope you find someone suitable.

Thanks,
Jamie
```

*(Note you need to change MY_NAME and COMPANY_NAME vars in auto.py)*
