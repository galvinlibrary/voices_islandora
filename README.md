# voices_islandora

This repo contains files related to a migration from a custom php site http://voices.iit.edu to Islandora 8 site at http://digital.library.iit.edu.


Migration Routine:
  * Import countries
    * `drush migrate-import some_id`
  * Import cities:
    * `drush migrate-import new_cities`
  * Import camps:
    * `drush migrate-import camp`
    * Add 'liberated by' manually
  * Import sub-camps:
    * `drush migrate-import subcamp`
  * Clean persons XML:
    * Remove xml namespaces from interview xml
      *`some command`
    * Swap voth codes for geographic taxonomy term names
      * `some command`
    * Swap nationality codes for geographic taxonomy term names
      * `some command`
  * Import Persons:
    * `drush migrate-import persons`
    
      
