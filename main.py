from reportlab.pdfgen import canvas

def save_to_pdf(product_names, quantities, prices, filename):
    pdf = canvas.Canvas(filename)
    pdf.setFont("Helvetica", 12)

    pdf.drawString(100, 750, "FINAL GROCERY LIST")
    y_position = 730  # starting y position for text
    for i in range(len(product_names)):
        y_position -= 15
        pdf.drawString(100, y_position, f"{product_names[i]} - Quantity: {quantities[i]}, Price: {prices[i]}")

    pdf.save()

def shopping_management_system():
    try:
        bg = float(input("Enter your budget: "))
        s = bg

        a = {"name": [], "quant": [], "price": []}
        b = list(a.values())
        na = b[0]
        qu = b[1]
        pr = b[2]

        while True:
            try:
                ch = int(input("1.ADD\n2.EXIT\nEnter your choice: "))
            except ValueError:
                print("\nERROR: Choose only digits from the given options")
                break

            if ch == 1 and s > 0:
                pn = input("Enter your product name: ")
                q = input("Enter your quantity: ")
                p = float(input("Enter price of the product: "))

                if p > s:
                    print("\nINSUFFICIENT BALANCE")
                    continue
                else:
                    if pn in na:
                        ind = na.index(pn)
                        qu[ind] = q
                        pr[ind] = p
                        s = bg - sum(pr)
                        print("\nAmount left: ", s)
                    else:
                        na.append(pn)
                        qu.append(q)
                        pr.append(p)
                        s = bg - sum(pr)
                        print("\nAmount left: ", s)

                    if s <= 0:
                        print("\nINSUFFICIENT BALANCE")
                        break

                    buy_more = input("\nDo you want to buy more? (1.yes/2.no): ").lower()
                    if buy_more != '1':
                        break

            print("\nAmount left: ", s)

            if s in pr:
                print("\nAmount left can get you a", na[pr.index(s)])

        print("\n\n\nFINAL GROCERY LIST")
        for i in range(len(na)):
            print(na[i], qu[i], pr[i])

        pdf_filename = "grocery_list.pdf"
        save_to_pdf(na, qu, pr, pdf_filename)
        print(f"\nGrocery list saved to {pdf_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    shopping_management_system()

