# Takács-Attila (H2GQZI)
3 modúl: random, time, tkinter

3 globális változó

7 definiíció:

	nyertesValaszt(generalt,mienk): Megkap egy random számot amit generálunk és összehasonlítja a mi választásunkkal.
	
	randomGeneral(): Létrehoz egy random számot 1-3 ig. Ez lesz az ellenfél választása, megváltoztatja a generált gomb szövegét.

	nyertesSzoveg(nyertes): Amikor vége egy körnek akkor ki írja az eredményt, plusz a statisztikát frissíti.

	idozito(masodperc): Ez a definíció felelős azért hogy visszaszámol 3 tól.

	jatek(valasztott): A játékmenetet bonyolítja le az előzően használt definíciók segítségével.

	Valasztott(valasztas): Az általunk választott gombot elhelyezi a választás után és elindítja a játékot.

	restart(): Az újraindításért felelős.

Kő Papir Olló játék, ahol egy AI ellen játszunk ami random kiválaszt egy lehetőséget a 3 közül és eldönti az ő, és a mi választásunk között, hogy

 nyertünk, döntetlen, vagy vesztettünk. Mindezt egy grafikus felületen amin látható az erdemény is statisztikán.
