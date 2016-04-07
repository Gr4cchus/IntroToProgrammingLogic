# Caffeine Absorption
degenerationRate = .87  # 13%

accumulator = 0
caffeineIntake = 130
while caffeineIntake > 65:
    accumulator += 1
    caffeineIntake *= degenerationRate
print("It will take", accumulator, "hours until caffeine half life.")

dailyCaffeine = 130
for hours in range(24):
    dailyCaffeine *= degenerationRate
print("After 24 hours there will be ", format(dailyCaffeine, '.2f'), "mg in the body.", sep="")

hourlyCaffeine = 0
for hours in range(24):
    hourlyCaffeine += 130
    if hours == 23:  # accept ingestion @ the last hour but no degeneration.
        break
    hourlyCaffeine *= degenerationRate
print("There will be ", format(hourlyCaffeine, '.2f'), "mg in the body after 24 hours.", sep="")
