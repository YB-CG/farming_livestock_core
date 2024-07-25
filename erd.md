# User (Farmer)
- UserID (Primary Key)
- FirstName
- LastName
- Email
- PasswordHash
- PhoneNumber
- DateOfBirth
- Gender
- Address
- City
- State/Province
- Country
- PostalCode

# Farm
- FarmID (Primary Key)
- UserID (Foreign Key, one-to-one relationship with User)
- FarmName
- Location

# Livestock
- LivestockID (Primary Key)
- FarmID (Foreign Key)
- AnimalType (e.g., Cow, Sheep, Pig)
- Breed
- Name (if applicable)
- TagNumber
- DateOfBirth
- Gender
- AcquisitionDate
- AcquisitionMethod (e.g., Born, Purchased)
- Status (e.g., Active, Sold, Deceased)
- CurrentWeight
- CurrentAge
- Photo (URL or file path)


# FeedingRecord
- FeedingRecordID (Primary Key)
- LivestockID (Foreign Key)
- FeedType
- Quantity
- Unit (e.g., kg, lbs)
- FeedingDate
- FeedingTime
- AdministeredBy (Foreign Key to User)
- Notes

# FeedInventory
- FeedInventoryID (Primary Key)
- FarmID (Foreign Key)
- FeedType
- Quantity
- Unit
- PurchaseDate
- ExpirationDate
- Supplier
- Cost
- Location (e.g., storage area)

# HealthRecord
- HealthRecordID (Primary Key)
- LivestockID (Foreign Key)
- RecordType (e.g., Illness, Vaccination, Routine Check)
- Date
- Description
- Diagnosis (if applicable)
- Treatment
- Medication
- Dosage
- AdministeredBy (Foreign Key to User)
- VeterinarianName (if applicable)
- FollowUpDate
- Outcome
- Notes

# BreedingRecord
- BreedingRecordID (Primary Key)
- MotherID (Foreign Key to Livestock)
- FatherID (Foreign Key to Livestock)
- BreedingDate
- ExpectedBirthDate
- ActualBirthDate
- NumberOfOffspring
- Notes

# Offspring
- OffspringID (Primary Key)
- BreedingRecordID (Foreign Key)
- LivestockID (Foreign Key - links to the Livestock table for the offspring's own record)
- BirthWeight
- BirthOrder
- Gender
- Status (e.g., Healthy, Weak, Deceased)

# Task
- TaskID (Primary Key)
- FarmID (Foreign Key)
- Title
- Description
- DueDate
- Priority (e.g., Low, Medium, High)
- Status (e.g., Pending, In Progress, Completed)
- AssignedTo (Foreign Key to User)
- RelatedEntityType (e.g., Livestock, Feeding, Health)
- RelatedEntityID
- CreationDate
- CompletionDate

# CalendarEvent
- EventID (Primary Key)
- FarmID (Foreign Key)
- Title
- Description
- StartDateTime
- EndDateTime
- Location
- EventType (e.g., Feeding, Health Check, Breeding, General)
- RelatedEntityType
- RelatedEntityID
- Reminder (Boolean)
- ReminderTime

# Notification
- NotificationID (Primary Key)
- UserID (Foreign Key)
- Title
- Message
- CreationDateTime
- ReadDateTime
- NotificationType (e.g., Task, Event, System)
- Priority (e.g., Low, Medium, High)
- RelatedEntityType
- RelatedEntityID

# InventoryItem
- InventoryItemID (Primary Key)
- FarmID (Foreign Key)
- ItemName
- ItemType (e.g., Equipment, Medicine, Supplies)
- Quantity
- Unit
- PurchaseDate
- ExpirationDate (if applicable)
- Supplier
- Cost
- Location
- MinimumStockLevel
- CurrentStockLevel

# FinancialTransaction
- TransactionID (Primary Key)
- FarmID (Foreign Key)
- Date
- Type (e.g., Income, Expense)
- Category (e.g., Feed Purchase, Livestock Sale, Equipment)
- Amount
- Description
- RelatedEntityType
- RelatedEntityID