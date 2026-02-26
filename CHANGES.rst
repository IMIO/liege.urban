Changelog
=========

.. You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst

.. towncrier release notes start

2.0.3 (2026-02-26)
------------------

Bug fixes:


- Fix missing access to voirie tab by voirie group
  [jchandelle] (SUP-51146)


2.0.2 (2026-02-24)
------------------

Bug fixes:


- Fix a display issue when address does not have a street number
  [mpeeters] (SUP-51118)


2.0.1 (2026-02-23)
------------------

Bug fixes:


- Ensure that `address_point` value is always an integer as expected by behavior schema
  [mpeeters] (SUP-51112)


Internal:


- Cleanup content factory module and remove unused imports
  [mpeeters] (SUP-51112)


2.0.0 (2026-02-17)
------------------

New features:


- Change back key dates display from liege
  [jchandelle] (SUP-49630)


Bug fixes:


- Fix string encoding worklocation signaletic
  [jchandelle] (SUP-49356)
- Fix CODT_UniqueLicence title encoding
  [jchandelle] (SUP-49359)
- Fix OpinionsRequest local role adapter
  Fix local role order
  Add test
  [jchandelle] (SUP-49445)
- Fix table encoding
  [jchandelle] (SUP-49474)
- Fix an issue with `address` indexed values where street numbers were missing
  [mpeeters] (SUP-49602)
- Fix list220 code ins getter
  [jchandelle] (SUP-49906)
- Add domain value in field to be translated in Product.urban
  [jchandelle] (SUP-49912)
- Fix possible infinite recursion with foldermanagers title
  [mpeeters] (SUP-50466)
- Avoid errors if there is no zip code, street or street number
  [mpeeters] (URB-3523)


Internal:


- Fix dashboard configs that are required to run tests
  [mpeeters] (SUP-49445)
- Fix initialization of tests
  [mpeeters] (URB-3522)


1.0.10 (2025-10-15)
-------------------

Bug fixes:


- Fix adapter for schedule collection icons
  [mpeeters] (URBBDC-3204)


1.0.9 (2025-07-27)
------------------

Bug fixes:


- Add an upgrade step for workflows, permissions and allowed content types
  [mpeeters] (SUP-45220)


1.0.8 (2025-06-05)
------------------

Bug fixes:


- Fix catalog query path for form_address in report
  [jchandelle] (SUP-45007)
- Fix missing import
  [aduchene] (URB-3258)


1.0.7 (2025-02-07)
------------------

New features:


- Modify obsolete state workflow and display order
  [jchandelle] (SUP-36697)


1.0.6 (2025-01-16)
------------------

New features:


- Adjust permissions on `codt_buildlicence_workflow` to handle `RoadReader` role.
  [aduchene]
  Add a new group `Voirie_readers` that can read all road decrees.
  [aduchene] (URBLIE-446)


Bug fixes:


- Don't dispatch on async instance in `MonthlyActivityReport`.
  [aduchene] (URB-3225)


1.0.5 (2024-10-17)
------------------

New features:


- Compatible with imio.pm.wsclient 2.x.
  [aduchene] (URB-3148)


1.0.4 (2024-10-01)
------------------

New features:


- Add form_composition field to the export in `activity_report.py`.
  [aduchene] (SUP-37960)


Bug fixes:


- Fix performance issue with `activity_report.py`.
  [aduchene] (URB-3102)


1.0.3 (2024-04-01)
------------------

New features:


- Add caduc workflow state
  [jchandelle,mpeeters] (URB-3007)
- Add frozen workflow state to article127, inspection and ticket
  [jchandelle] (URB-3023)


Bug fixes:


- Fix an issue with zope users on urban homepage
  [mpeeters] (URB-2956)


1.0.2 (2023-11-21)
------------------

Bug fixes:


- Ensure that every licence types can add `UrbanEventMayor` and `UrbanEventAcknowledgment`
  [mpeeters] (SUP-33677)


1.0.1 (2023-11-16)
------------------

- Fix template for worklocation [URB-2930]
  [mpeeters]


1.0.0 (2023-11-09)
------------------

- Add get_work_location method.
  [fngaha]

- Initial release.
  [sdelcourt]
