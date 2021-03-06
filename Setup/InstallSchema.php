<?php

namespace tutorial\nvphuong\Setup;

use Magento\Framework\Setup\InstallSchemaInterface;
use Magento\Framework\Setup\ModuleContextInterface;
use Magento\Framework\Setup\SchemaSetupInterface;
use Magento\Framework\DB\Ddl\Table;

class InstallSchema implements InstallSchemaInterface
{
	public function install(SchemaSetupInterface $setup, ModuleContextInterface $context)
	{
		$setup->startSetup();
		$tableName = $setup->getTable('Custom_table');
		if ($setup->getConnection()->isTableExists($tableName)!=true) {
			$table = $setup->getConnection()->newTable($tableName)
				->addColumn(
					'id',
					Table::TYPE_INTEGER,
					null,
					[
						'identity'=>true,
						'unsigned'=>true,
						'nullable'=>false,
						'primary'=>true
					],
					'ID'
				)
				->addColumn(
					'title',
					Table::TYPE_TEXT,
					null,
					['nullable'=>true,'default'=>''],
					'Title'
				)
				->addColumn(
					'description',
					Table::TYPE_TEXT,
					null,
					['nullable'=>true,'default'=>''],
					'Description'
				)
				->addColumn(
					'image',
					Table::TYPE_TEXT,
					null,
					['nullable'=>true,'default'=>''],
					'Image'
				)
				->addColumn(
					'status',
					Table::TYPE_SMALLINT,
					null,
					['nullable'=>false,'default'=>'0'],
					'Status'
				)
				->addColumn(
					'create_at',
					Table::TYPE_DATETIME,
					null,
					['nullable'=>false],
					'Create at'
				)
				->addColumn(
					'update_at',
					Table::TYPE_TEXT,
					null,
					['nullable'=>false],
					'Update at'
				)
				->setComment('Custom_table_comment')
				->setOption('type', 'InnoDB')
				->setOption('charset', 'utf8');
			$setup->getConnection()->createTable($table);
		}
		$setup->endSetup();
	}
}
