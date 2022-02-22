import json

HTMLString = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link
            href="https://fonts.googleapis.com/icon?family=Material+Icons"
            rel="stylesheet"
        />
        <link rel="stylesheet" href="../dist/output.css" />
        <title>IEEE IIITD Member - {tname}</title>
    </head>
    <body class="flex flex-col md:min-h-screen">
       <!-- header -->
        <header class="header">
            <nav class="nav">
                <div class="mx-auto my-5 max-w-xl container">
                    <div class="flex justify-between items-center px-4 md:px-8 xl:px-0">
                        <div class="flex items-center">
                            <a href="../index.html">
                                <img
                                    src="../assets/index/logo.png"
                                    alt="logo"
                                    class="h-12"
                                />
                            </a>
                        </div>
                        <div class="flex items-center">
                            <a href="../events.html" class="heading2 px-4 py-2"
                                >events</a
                            >
                            <a href="../members.html" class="heading2 pl-4 py-2"
                                >members</a
                            >
                        </div>
                    </div>
                </div>
            </nav>
        </header>

        <!-- main -->
        <main class="flex-auto">
            <!-- details -->
            <section id="details" class="md:min-h-screen">
                <div class="container mx-auto mt-40">
                    <div class="flex flex-col">
                        <div class="flex flex-col md:flex-row justify-around">
                            <div class="memPgImg flex flex-col">
                                <h3 class="text-sm text-gray-500 font-semibold"><a href="../members.html" class="text-sm text-gray-500 font-semibold">members</a> / {sname}</h6>
                                <img src="{img}" alt="{aname}" class="rounded-xl mt-10" />
                                <div class="flex flex-row justify-between mt-7">
                                    <img src="https://via.placeholder.com/50x50" alt="" class="rounded-full"/>
                                    <img src="https://via.placeholder.com/50x50" alt="" class="rounded-full"/>
                                    <img src="https://via.placeholder.com/50x50" alt="" class="rounded-full"/>
                                </div>
                            </div>
                            <div class="memPgTxt flex flex-col w-32 space-y-5 mt-10">
                                <h1 class="heading text-5xl">{name}</h1>
                                <h2 class="text-3xl font-semibold text-gray-500">{pos}</h2>
                                <p class="text-gray-500 leading-10">
                                    {desc}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- contact -->
            <section id="contact" class="footer-bg">
                <div class="container w-11/12 mx-auto">
                    <div
                        class="mx-auto flex flex-col md:flex-row gap-10 text-white py-20 justify-between max-w-lg md:max-w-none w-full space-y-5"
                    >
                        <a href="" class="memAlum flex flex-col p-7 justify-end items-end text-right rounded-xl">
                                <h1 class="heading text-3xl font-bold">
                                    Our Members and Alumni
                                </h1>
                                
                                <div
                                    class="rounded-full border-1 py-2 px-2 flex justify-center items-center mt-7"
                                    style="background: #f8f8f870"
                                >
                                    <i class="material-icons text-white">
                                        keyboard_arrow_right
                                    </i>
                                </div>
                        </a>
                        <div class="flex flex-col justify-center">
                            <h1
                                class="fancyJoin heading text-4xl md:text-4xl font-bold leading-10"
                            >
                                Join Us.
                            </h1>
                            
                            <h2
                                class="heading text-2xl md:text-3xl xl:text-4xl font-bold w-full md:w-1/2 mt-3"
                            >
                                Become a part of the exclusive community.
                            </h2>
                            
                            <h3 class="font-bold mt-6">Perks</h3>
                            <ul class="text-gray-500">
                                <li>
                                    Lorem ipsum dolor sit amet consectetur
                                    adipisicing elit.
                                </li>
                                <li>
                                    Lorem ipsum dolor sit amet consectetur
                                    adipisicing elit.
                                </li>
                                <li>
                                    Lorem ipsum dolor sit amet consectetur
                                    adipisicing elit.
                                </li>
                            </ul>
                            
                            <a href="" class="heading2 applyBtn bg-white px-10 py-2 text-black rounded-lg mt-10 w-1/4 text-center min-w-[128px]">
                                    apply
                            </a>
                        </div>
                    </div>
                    <hr class="border-gray-500 rounded-full mx-auto linejoin" />
                </div>
            </section>
        </main>

        <!-- footer -->
        <footer class="footer-bg px-8">
            <div class="container mx-auto my-14 mb-28">
                <div
                    class="flex flex-col md:flex-row gap-4 md:gap-8 md:justify-between text-white md:mx-auto space-y-5 mx-auto max-w-lg md:max-w-none"
                >
                    <div
                        class="flex flex-row gap-4 w-full min-w-fit md:w-1/4 md:mx-auto"
                    >
                        <div class="flex pt-4 text-white">
                            <img
                                src="../assets/index/logowhite.png"
                                alt="logo"
                                class="footerLogo"
                            />
                        </div>
                        <div class="flex flex-col md:justify-center">
                            <h1 class="heading text-xl font-bold">IEEE</h1>
                            <h1 class="heading text-xl font-bold">
                                IIIT Delhi
                            </h1>
                            <h2 class="heading text-md font-bold text-gray-500">
                                student branch
                            </h2>
                            
                            <p class="text-sm text-gray-500 mt-3">
                                IIIT Delhi, Okhla Industrial, <br />
                                Phase-III, New Delhi-110020
                            </p>
                        </div>
                    </div>
                    <div
                        class="flex flex-col md:flex-row gap-4 md:gap-16 md:justify-between w-full md:w-1/3 md:mx-auto"
                    >
                        <div class="flex flex-col w-full md:w-1/2 mb-5 md:mb-5">
                            <h1 class="heading font-bold">Affiliations</h1>
                            <div
                                class="flex flex-wrap md:flex-col space-x-5 md:space-x-0"
                            >
                                <a href="https://iiitd.ac.in/" target="blank" class="text-gray-500"><span class="link link-underline link-underline-black">IIIT Delhi</span></a>
                                <a href="https://www.ieee.org/" target="blank" class="text-gray-500"><span class="link link-underline link-underline-black">IEEE</span></a>
                                <a href="https://www.wie.ieee.org/" target="blank" class="text-gray-500"><span class="link link-underline link-underline-black">WiE</span></a>
                                <a href="https://www.computer.org/" target="blank" class="text-gray-500"><span class="link link-underline link-underline-black">CompSoc</span></a>
                            </div>
                        </div>
                        <div class="flex flex-col w-full md:w-1/2">
                            <h1 class="heading font-bold">Socials</h1>
                            <div
                                class="flex flex-wrap md:flex-col md:space-x-0"
                            >
                                <a href="https://www.instagram.com/ieeeiiitdelhi/" target="blank" class="pr-5 md:pr-0 text-gray-500"><span class="link link-underline link-underline-black">Instagram</span></a>
                                <a href="https://www.facebook.com/ieeeiiitd/" target="blank" class="pr-5 md:pr-0 text-gray-500"><span class="link link-underline link-underline-black">Facebook</span></a>
                                <a href="https://www.linkedin.com/company/ieee-iiitd/" target="blank" class="pr-5 md:pr-0 text-gray-500"><span class="link link-underline link-underline-black">LinkedIn</span></a>
                                <a href="https://www.youtube.com/channel/UCKqQYeZ_yOSWL0BQ7eWUqRA" target="blank" class="pr-5 md:pr-0 text-gray-500"><span class="link link-underline link-underline-black">YouTube</span></a>
                                <a href="https://twitter.com/ieee_d/" target="blank" class="pr-5 md:pr-0 text-gray-500"><span class="link link-underline link-underline-black">Twitter</span></a>
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-col w-full md:w-1/5">
                        <h1 class="heading font-bold">Contact</h1>
                        <p class="text-gray-500">
                            <a href="mailto:ieee@iiitd.ac.in"
                                >ieee@iiitd.ac.in</a
                            >
                        </p>
                        
                        <h1 class="heading font-bold mt-3">Graphic Identity</h1>
                    </div>
                </div>
            </div>
        </footer>
    </body>
</html>
"""

f = open('members.json')

data = json.load(f)

BASE_DIR = "./members/"

print("PROCESS STARTED")
print("PROCESSING ...")
# print(HTMLString.format(name = data[26]["name"]), pos = data[26]["pos"], img = data[26]["img"], desc = data[26]["desc"])
for i in range(len(data)):
    f = open(BASE_DIR + str(i+1) + ".html", "w")
    tname = data[i]["name"]
    sname = data[i]["name"]
    img = '.'+data[i]["img"]
    aname = data[i]["name"]
    name = data[i]["name"]
    pos = data[i]["pos"]
    desc = data[i]["desc"]
    f.write(HTMLString.format(tname = tname, sname = sname, aname = aname, name = name, pos = pos, img = img, desc = desc))
    f.close()
print("PROCESS COMPLETED")
