# Övning - preamble

- Vår gamla kod från förra veckan är uppdaterad enligt vad vi gjorde på föreläsningen idag: Vi har nu separata Model, View och Controller, som var och en gör det som förväntas av dem. Nästan.
- Uppföljning från gamla ämnet: Animeringen fungerar inte. Vyn uppdateras inte förrän man klickar i den. Vad är fel? Rätta felet. Hint: Det saknas en enda rad kod.
- För resten av övningen, fokusera på paketet shapes. Vi struntar för den här övningen i hur det sen ska användas – du har nu hatten av maintainer för detta paket, och vet ingenting om `DrawPolygons`.

# Övning

- Klassen `Shape` har ett väldefinierat gränssnitt. Denna klass är definitivt muterbar (än så länge). Men på grund av att `Point` också är muterbar, kan en `Shape` flyttas indirekt på annat sätt än som är tänkt via gränssnittet. 
  - Förstå hur detta ”trick” går till. Fundera över olika sätt vi skulle kunna lösa det.
- Ett (eller egentligen två) sätt är att definiera en egen, immutable, `Point`-klass. Detta kan antingen göras helt från scratch, eller genom att skapa en immutable wrapper runt den existerande `Point`-klassen. Testa båda dessa lösningar.
- Lös problemet även utan att definiera en egen `Point`-klass, och utan att förändra gränssnittet för `Shape`. Jo, det går!
- Även `Shape` i helhet kan göras immutable, och ändå tillåta translation, skalning och rotation. Sättet vi gör det på är att vi, istället för att uppdatera det egna objektet, returnera en ny kopia med de nya värdena. Retur-typerna för de tre ”muterande” metoderna blir alltså `Shape`, istället för `void` som nu. 
  - Vilka för- respektive nackdelar har denna lösning jämfört med ovanstående?
