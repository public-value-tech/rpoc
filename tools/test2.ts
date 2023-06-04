import { Client } from '@microsoft/microsoft-graph-client';
import { TokenCredentialAuthenticationProvider } from '@microsoft/microsoft-graph-client/authProviders/azureTokenCredentials';
import { DeviceCodeCredential } from '@azure/identity';

const credential = new DeviceCodeCredential({
  tenantId: 'insert_tenant_id_here',
  clientId: 'insert_client_id_here',
});

const authProvider = new TokenCredentialAuthenticationProvider(credential, {
  scopes: ['insert_scopes_here'],
});

const client = Client.initWithMiddleware({
  debugLogging: true,
  authProvider,
});

const client = Client.init(options);

let worksheets = await client.api('/me/drive/items/70C7E11E-66A6-4AEC-AAC7-DD0E3B77B297/workbook/worksheets')
	.get();