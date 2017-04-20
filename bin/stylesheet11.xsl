<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="text"/>
  <xsl:template match="/">

    <xsl:for-each select="TaxaSet/Taxon">
      <xsl:value-of select="TaxId"/>
      <xsl:text>&#009;</xsl:text>
      <xsl:apply-templates select="ScientificName"/>
      
      <xsl:text>&#009;</xsl:text>
      <xsl:apply-templates select="OtherNames/Synonym[1]"/>


     <xsl:for-each select="LineageEx/Taxon">
     <xsl:if test="((Rank = 'genus'))">
        <xsl:text>&#009;</xsl:text>
        <xsl:value-of select="ScientificName"/>
      </xsl:if>
      </xsl:for-each>


    <xsl:for-each select="LineageEx/Taxon">
     <xsl:if test="((Rank = 'family'))">
        <xsl:text>&#009;</xsl:text>
        <xsl:value-of select="ScientificName"/>
      </xsl:if>
      </xsl:for-each>


    <xsl:for-each select="LineageEx/Taxon">
     <xsl:choose>
      <xsl:when test="((Rank = 'order'))">
        <xsl:text>&#009;</xsl:text>
        <xsl:value-of select="ScientificName"/>
      </xsl:when>
      <xsl:when test="((Rank = 'infraorder'))">
        <xsl:text>&#009;</xsl:text>
        <xsl:value-of select="ScientificName"/>
      </xsl:when>
     </xsl:choose>
     </xsl:for-each>


<xsl:text>
</xsl:text>

  </xsl:for-each>

</xsl:template>
</xsl:stylesheet>
