text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')
piece = text[pos+1 : ]
stripped = piece.strip()
flt = float(stripped)
print(flt)